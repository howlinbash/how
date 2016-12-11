#! /usr/bin/python3

import subprocess

from lib.db import tags
from lib.argparser import args, parser

manual_path = "/home/howlin/src/manual/"

def edit_page(page_path):
    command = manual_path + page_path
    subprocess.call(['vim', command])

def list_tags():
    col_width = max(len(tag) for tag in tags) + 2

    for x in sorted(tags):
        print (x.ljust(col_width), tags[x])

def list_pages():
    program = "tree "
    options = " --noreport -C --dirsfirst -I "
    excluded_files = "\"" \
        + "home.md" + "|" \
        + "howlin-wolf-square-tiny.jpg" + "|" \
        + "index.md" + "|" \
        + "latest.md" + "|" \
        + "template.md" + "|" \
        + "README.md" + "|" \
        + "pipeline" \
        + "\""
    argument = program + manual_path + options + excluded_files
    subprocess.call(argument, shell=True)

def open_page(page_path):
    url = "file:///" + manual_path + page_path
    subprocess.call(['chromium', url])

def get_page_path(arg):
    return str(tags.get(arg, 0))

if args.edit:
    edit_page(get_page_path(args.edit[0]))
elif args.list_pages:
    list_pages()
elif args.list_tags:
    list_tags()
elif args.tag:
    open_page(get_page_path(args.tag))
else:
    parser.print_help()
