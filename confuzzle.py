import sys
import argparse
import yaml
from jinja2 import Template


def render(template_string, context_dict):
    template = Template(template_string)
    return template.render(**context_dict)


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('template', nargs='?', type=argparse.FileType('r'), default=sys.stdin, help="Config file template. If not supplied, stdin is used")
    parser.add_argument('config', type=argparse.FileType('r'), help="YAML data file to read")
    parser.add_argument('--out', '-o', dest='out', type=argparse.FileType('w'), default=sys.stdout, help="Output file to write. If not supplied, stdout is used")

    args = parser.parse_args()

    context_dict = yaml.load(args.config.read())
    template_string = args.template.read()

    rendered = render(template_string, context_dict)
    args.out.write(rendered)


if __name__ == "__main__":
    main()
