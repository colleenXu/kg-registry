#!/usr/bin/env python3

import argparse
import logging
import sys
import time
from contextlib import closing
from json import dumps

import requests
import yaml
from SPARQLWrapper import JSON, SPARQLWrapper

__author__ = "cjm"


def main():
    parser = argparse.ArgumentParser(
        description="Helper utils for KG-Registry",
        formatter_class=argparse.RawTextHelpFormatter,
    )
    parser.add_argument(
        "-i", "--input", type=str, required=False, help="Input metadata file"
    )
    parser.add_argument(
        "-v",
        "--verbosity",
        default=0,
        action="count",
        help="Increase output verbosity (min.: 0, max. 2)",
    )
    subparsers = parser.add_subparsers(dest="subcommand", help="sub-command help")

    # SUBCOMMAND
    parser_n = subparsers.add_parser("check-urls", help="Ensure PURLs resolve")
    parser_n.set_defaults(function=check_urls)

    parser_n = subparsers.add_parser(
        "sparql-compare",
        help="Run SPARQL commands against the db to generate a " "consistency report",
    )
    parser_n.set_defaults(function=sparql_compare_all)

    parser_n = subparsers.add_parser("extract-context", help="Extracts JSON-LD context")
    parser_n.set_defaults(function=extract_context)

    parser_n = subparsers.add_parser(
        "extract-contributors",
        help="Queries github API for metadata about contributors",
    )
    parser_n.set_defaults(function=write_all_contributors)

    args = parser.parse_args()
    if args.verbosity >= 2:
        logging.basicConfig(level=logging.DEBUG)
    elif args.verbosity == 1:
        logging.basicConfig(level=logging.INFO)
    else:
        logging.basicConfig(level=logging.WARNING)

    with open(args.input, "r") as f:
        obj = yaml.load(f, Loader=yaml.SafeLoader)
        resources = obj["resources"]

    func = args.function
    func(resources, args)


def check_urls(resources, args):
    """
    Ensure PURLs resolve
    """

    def test_url(url):
        try:
            with closing(requests.get(url, stream=False)) as resp:
                return resp.status_code == 200
        except requests.exceptions.InvalidSchema as e:
            # TODO: requests lib doesn't handle ftp. For now simply return True in that case.
            if not format(e).startswith("No connection adapters were found for 'ftp:"):
                raise
            return True

    failed_ids = []
    for ont in resources:
        for p in ont.get("products", []):
            pid = p["id"]
            if not test_url(p.get("resource_purl")):
                failed_ids.append(pid)
    if len(failed_ids) > 0:
        print("FAILURES:")
        for pid in failed_ids:
            print(pid, file=sys.stderr)
        exit(1)


def extract_context(resources, args):
    """
    Writes to STDOUT a sorted JSON map from resource prefixes to PURLs
    """

    def has_obo_prefix(obj):
        return ("uri_prefix" not in obj) or (
            obj["uri_prefix"] == "http://purl.obolibrary.org/obo/"
        )

    prefix_map = {}
    for obj in resources:
        if has_obo_prefix(obj):
            prefix = obj.get("preferredPrefix") or obj["id"].upper()
            prefix_map[prefix] = {
                "@id": "http://purl.obolibrary.org/obo/" + prefix + "_",
                "@prefix": True,
            }

    print(
        dumps(
            {"@context": prefix_map}, sort_keys=True, indent=4, separators=(",", ": ")
        )
    )


def write_all_contributors(resources, args):
    """
    Query github API for all contributors to a resource,
    write results as json
    """
    results = []
    for ont_obj in resources:
        id = ont_obj["id"]
        logging.info("Getting info for {}".format(id))
        repo_path = get_repo_path(ont_obj)
        if repo_path is not None:
            contribs = list(get_resource_contributors(repo_path))
            print("CONTRIBS({})=={}".format(id, contribs))
            for c in contribs:
                print("#{}\t{}\n".format(id, c["login"]))
            results.append(dict(id=id, contributors=contribs))
        else:
            logging.warn("No repo_path declared for {}".format(id))
    print(dumps(results, sort_keys=True, indent=4, separators=(",", ": ")))


def get_resource_contributors(repo_path):
    """
    Get individual contributors to a org/repo_path
    repo_path is a string "org/repo"
    """
    url = "https://api.github.com/repos/{}/contributors".format(repo_path)
    # TODO: allow use of oauth token;
    # GH has a quota for non-logged in API calls
    time.sleep(3)
    with closing(requests.get(url, stream=False)) as resp:
        ok = resp.status_code == 200
        if ok:
            results = resp.json()
            logging.info("RESP={}".format(results))
            return results
        else:
            logging.error("Failed: {}".format(url))
            return []


def get_repo_path(ont_obj):
    """
    Extract the repository path for the given object
    """
    repo_path = None
    if "repository" in ont_obj:
        repo_path = ont_obj["repository"]
    elif "tracker" in ont_obj:
        tracker = ont_obj["tracker"]
        if tracker is not None and "github" in tracker:
            repo_path = tracker.replace("/issues", "")

    if repo_path is not None:
        repo_path = repo_path.replace("https://github.com/", "")
        if repo_path.endswith("/"):
            repo_path = repo_path[:-1]
        return repo_path
    else:
        logging.warn("Could not get gh repo_path for ".format(ont_obj))
        return None


def run_sparql(obj, p, expected_value, q):
    """
    Generate a SPARQL statement using query q and parameter p, and expect 'expected_value' as the
    result. Print out a message indicating whether the there is or is not a match for the given object
    """
    sparql = SPARQLWrapper("http://sparql.hegroup.org/sparql")
    sparql.setQuery(q)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    id = obj["id"]
    got_value = False
    is_match = False
    vs = []

    for result in results["results"]["bindings"]:
        got_value = True
        v = result[p]["value"]
        vs.append(str(v))
        if v == expected_value:
            is_match = True

    if got_value and is_match:
        msg = "CONSISTENT"
    elif got_value and not is_match:
        if expected_value == "":
            msg = "UNDECLARED_LOCAL: REMOTE:" + ",".join(vs)
        else:
            msg = "INCONSISTENT: REMOTE:" + ",".join(vs) + " != LOCAL:" + expected_value
    else:
        msg = "UNDECLARED_REMOTE"
    print(id + " " + p + " " + msg)


if __name__ == "__main__":
    main()
