#! /usr/bin/python3

import subprocess
import sys

from lib.db import tags
from lib.argparser import args, parser

manual_path = "/home/howlin/src/manual/"
editor = 'nvim'

def open_page(page_path):
    command = manual_path + page_path
    subprocess.call([editor, command])

def list_tags():
    col_width = max(len(tag) for tag in tags) + 2

    for x in sorted(tags):
        print (x.ljust(col_width), tags[x])

def print_contents():
    program = "tree "
    options = " --noreport -C --dirsfirst -I "
    excluded_files = "\"" \
        + "howlin-wolf-square-tiny.jpg" + "|" \
        + "index.md" + "|" \
        + "latest.md" + "|" \
        + "list_index.md" + "|" \
        + "tags" + "|" \
        + "template.md" + "|" \
        + "README.md" + "|" \
        + "LICENSE.md" + "|" \
        + "pipeline" \
        + "\""
    argument = program + manual_path + options + excluded_files
    subprocess.call(argument, shell=True)

def view_page(page_path):
    url = "file:///" + manual_path + page_path
    subprocess.call(['chromium', url])

def get_page_path(arg):
    return str(tags.get(arg, 0))

if len(sys.argv) == 1:
    open_page('index.md')
elif args.view:
    view_page(get_page_path(args.view[0]))
elif args.print_contents:
    print_contents()
elif args.list_tags:
    list_tags()
elif args.tag:
    open_page(get_page_path(args.tag))
else:
    parser.print_help()
