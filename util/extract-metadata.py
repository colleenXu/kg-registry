#!/usr/bin/env python3

import argparse
import sys
import pathlib

import frontmatter
import yaml
from copy import deepcopy
from frontmatter.util import u
from linkml.validator import validate
from ruamel.yaml import YAML
from ruamel.yaml.compat import StringIO
from yamllint import config, linter

__author__ = "cjm"
HERE = pathlib.Path(__file__).parent.resolve()
ROOT = HERE.parent.resolve()
SOURCE_SCHEMA_PATH = ROOT.joinpath(
    "src", "kg_registry", "kg_registry_schema", "schema", "kg_registry_schema.yaml")
SCHEMA_PATH = ROOT.joinpath("src", "kg_registry", "kg_registry_schema", "kg_registry_schema.json")


def main():
    parser = argparse.ArgumentParser(
        description="Helper utils for KG-Registry",
        formatter_class=argparse.RawTextHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="subcommand", help="sub-command help")

    # SUBCOMMAND
    parser_n = subparsers.add_parser("validate", help="validate yaml inside md")
    parser_n.set_defaults(function=validate_markdown)
    parser_n.add_argument("files", nargs="*")
    parser_n = subparsers.add_parser(
        "prettify", help="prettify YAML block in registry Markdown files"
    )
    parser_n.set_defaults(function=prettify)
    parser_n.add_argument("files", nargs="*")
    # SUBCOMMAND
    parser_n = subparsers.add_parser("concat", help="concat resource yamls")
    parser_n.add_argument("-i", "--include", help="yaml file to include for header")
    parser_n.add_argument("-o", "--output", help="output yaml file")
    parser_n.set_defaults(function=concat_resource_yaml)
    parser_n.add_argument("files", nargs="*")

    args = parser.parse_args()

    func = args.function
    func(args)


class CustomRuamelYAMLHandler(frontmatter.YAMLHandler):
    def __init__(self):
        self.myyaml = YAML()
        self.myyaml.default_flow_style = False
        self.myyaml.allow_duplicate_keys = True
        self.myyaml.indent(mapping=2, sequence=4, offset=2)
        self.myyaml.preserve_quotes = True
        self.myyaml.width = 1500
        # self.myyaml.explicit_start = True
        super().__init__()

    def load(self, fm, **kwargs):
        return self.myyaml.load(fm, **kwargs)

    def export(self, metadata, **kwargs):
        stream = StringIO()
        self.myyaml.dump(data=metadata, stream=stream)
        metadata = stream.getvalue()
        metadata = metadata[:-1]
        return u(metadata)


def prettify(args):
    for file in args.files:
        handler = CustomRuamelYAMLHandler()
        text = frontmatter.load(file, handler=handler)
        file_obj = open(file, "wb")
        frontmatter.dump(text, fd=file_obj, handler=handler)
        file_obj = open(file, "a")
        file_obj.write("\n")
        file_obj.close()


def validate_markdown(args):
    """
    Ensure the yaml encoded inside a YAML file is syntactically valid.

    First attempt to strip the yaml from the .md file, second use the standard python yaml parser
    to parse the embedded yaml. If it can't be passed then an error will be thrown and a stack
    trace shown.

    This also uses the LinkML schema to validate the yaml.
    """

    errs = []
    warn = []
    for fn in args.files:
        # Check to see if we can parse the yaml frontmatter first
        if not frontmatter.check(fn):
            errs.append("%s does not contain frontmatter" % (fn))

        # Run LinkML validator
        # Different objects need to be validated against different
        # parts of the schema
        (obj, md) = load_md(fn)

        # If this is the root of the resource, validate against the Resource class
        # These pages will already contain child classes, so other
        # pages don't need their own validation (it would be redundant)
        if obj.get("id") == pathlib.Path(fn).parent.name:
            target_class = "Resource"
        else:
            continue
        report = validate(instance=obj, schema=SOURCE_SCHEMA_PATH, target_class=target_class)
        if report.results:
            for result in report.results:
                if result.severity == "ERROR":
                    errs.append(f"{fn}: {result.message}")

        # Now run yaml linter to check for basic syntax errors and formatting
        yamltext = get_YAML_text(fn)
        yaml_config = config.YamlLintConfig(file="util/config.yamllint")
        for p in linter.run("---\n" + yamltext, yaml_config):
            if p.level == "error":
                errs.append(f"%s: {p}" % (fn))
            elif p.level == "warning":
                warn.append(f"%s: {p}" % (fn))

    if len(warn) > 0:
        print("WARNINGS:", file=sys.stderr)
        for w in warn:
            print("WARN: " + w, file=sys.stderr)
    if len(errs) > 0:
        print("FAILURES:", file=sys.stderr)
        for e in errs:
            print("ERROR:" + e, file=sys.stderr)
        sys.exit(1)


def concat_resource_yaml(args):
    """
    Given arguments with files and ouput,
    read YAML files into an array and write an output YAML file.
    Output will be concatenated list of all resource metadata.
    Assumes that args.files is already sorted alphabetically.

    This function also:
    * Creates sub-pages for products as needed
    * Propagates derived products to the source Resource pages
    * Adds a logo to the license metadata if it exists
    """

    def decorate_metadata(objs):
        """
        Add the logo corresponding to the given object's license (if it has one).
        """

        for obj in objs:
            if "license" in obj:
                # https://creativecommons.org/about/downloads
                license = obj["license"]
                try:
                    lurl = license["id"]  # This should be a URL
                except KeyError:
                    print(f"ERROR: Could not find id for license in {obj['id']}")
                    sys.exit(1)
                logo = ""
                if lurl.find("creativecommons.org/licenses/by-sa") > 0:
                    logo = (
                        "https://mirrors.creativecommons.org/presskit/buttons/80x15/png/by-sa.png"
                    )
                elif lurl.find("creativecommons.org/licenses/by/") > 0:
                    logo = "http://mirrors.creativecommons.org/presskit/buttons/80x15/png/by.png"
                elif lurl.find("creativecommons.org/publicdomain/zero/") > 0:
                    logo = (
                        "http://mirrors.creativecommons.org/presskit/buttons/80x15/png/cc-zero.png"
                    )
                if logo:
                    license["logo"] = logo

    def generate_product_pages(objs):
        layout_string = "layout: product_detail"
        for obj in objs:
            if "products" in obj:
                for product in obj["products"]:
                    # Only create pages for products with IDs that start with the resource ID
                    if "id" in product and (product["id"]).startswith(obj["id"]):
                        fn = f"resource/{obj['id']}/{product['id']}.md"
                        file_path = pathlib.Path(fn)

                        # Create a copy of the product to add layout
                        product_with_layout = deepcopy(product)

                        # Check if file exists
                        if file_path.exists():
                            try:
                                # Load existing product data
                                existing_product = frontmatter.load(fn).metadata

                                # Remove layout from comparison if it exists
                                existing_product_copy = deepcopy(existing_product)
                                if "layout" in existing_product_copy:
                                    del existing_product_copy["layout"]

                                # Compare content (ignoring order)
                                if yaml.dump(sorted(product.items())) == yaml.dump(sorted(existing_product_copy.items())):
                                    continue
                                else:
                                    print(
                                        f"Updating page for product {product['id']} - content changed")
                                    # Show what's different
                                    product_keys = set(product.keys())
                                    existing_keys = set(existing_product_copy.keys())

                                    # Show added or removed keys
                                    added_keys = product_keys - existing_keys
                                    removed_keys = existing_keys - product_keys
                                    if added_keys:
                                        print(f"  Added fields: {', '.join(added_keys)}")
                                    if removed_keys:
                                        print(f"  Removed fields: {', '.join(removed_keys)}")

                                    # Show changed values for common keys
                                    common_keys = product_keys.intersection(existing_keys)
                                    for key in common_keys:
                                        if product[key] != existing_product_copy.get(key):
                                            print(f"  Changed '{key}'")
                            except Exception as e:
                                print(
                                    f"Error reading existing product file {fn}, will recreate: {str(e)}")
                        else:
                            print(f"Creating new page for product {product['id']}")

                        # Write the product to its own page
                        with open(fn, "w") as f:
                            f.write("---\n" + yaml.dump(product) + layout_string + "\n---\n")

    def propagate_products(objs):
        """
        Propagates derived products to their source Resource pages.
        For example, if the page for Aggregator A lists a product from Source S,
        then the page for Source S should list Aggregator A's version of it as a derived product.
        """

        to_be_propagated = {}

        # Search for applicable derived products first
        for obj in objs:
            if "products" in obj:
                for product in obj["products"]:
                    for field_name in ["original_source", "secondary_source"]:
                        if field_name in product:
                            for resource_id in product[field_name]:
                                if resource_id != obj["id"]:
                                    if resource_id not in to_be_propagated:
                                        to_be_propagated[resource_id] = []
                                    to_be_propagated[resource_id].append(deepcopy(product))
        print(
            f"Found {len(to_be_propagated)} resources with products to propagate: {', '.join(to_be_propagated.keys())}")

        # Now update the concatenated list of resources
        # And write newly added products to their respective Resource pages
        print("Cross-resource references:")
        print("Resource Name\tCount of products referencing")
        for obj in objs:
            if obj["id"] in to_be_propagated:
                print(f"{obj['id']}\t{len(to_be_propagated[obj["id"]])}")

                total_written = 0

                if "products" not in obj:
                    obj["products"] = []

                # Do the writing here
                for product in to_be_propagated[obj["id"]]:

                    # Write to the concatenated list of resources
                    if product not in obj["products"]:
                        obj["products"].append(product)
                        total_written += 1

                    # Write to the respective Resource page
                    fn = f"resource/{obj['id']}/{obj['id']}.md"
                    (metadata, md) = load_md(fn)
                    if "products" not in metadata:
                        metadata["products"] = []
                    if product not in metadata["products"]:
                        metadata["products"].append(product)
                    with open(fn, "w") as f:
                        f.write("---\n" + yaml.dump(metadata) + "---\n" + md)

                if total_written > 0:
                    print(f" Wrote {str(total_written)} product(s) to {obj['id']} entry")

    objs = []
    foundry = []
    library = []
    obsolete = []
    cfg = {}
    if args.include:
        with open(args.include, "r") as f:
            cfg = yaml.load(f.read(), Loader=yaml.SafeLoader)
    for fn in args.files:
        (obj, md) = load_md(fn)
        # Check if the object is actually a product
        if obj.get("id") == pathlib.Path(fn).parent.name:
            library.append(obj)
    objs = foundry + library + obsolete
    cfg["resources"] = objs

    # Generate product pages
    generate_product_pages(objs)

    # Propagate derived products to the source Resource pages
    propagate_products(objs)

    # Add logos to licenses
    decorate_metadata(objs)

    with open(args.output, "w") as f:
        f.write(yaml.dump(cfg))
    return cfg


def load_md(fn):
    """
    Load a yaml text blob from a markdown file and parse the blob.

    Returns a tuple (yaml_obj, markdown_text)
    """
    onto_stuff = frontmatter.load(fn)
    return (onto_stuff.metadata, onto_stuff.content)


def get_YAML_text(fn):
    with open(fn, "r") as f:
        text = f.read()
        chunks = text.split("---")
        yamltext = chunks[1].strip()
        return yamltext


if __name__ == "__main__":
    main()
