#! /usr/bin/python3

import subprocess

from lib.db import tags
from lib.parser import args

manual_path = "/home/howlin/src/manual/"

def open_page(page_path):
    url = "file:///" + manual_path + page_path
    subprocess.call(['chromium', url])

def edit_page(page_path):
    command = manual_path + page_path
    subprocess.call(['vim', command])

tag = args.tag

page_path = str(tags.get(tag, 0))

if args.edit:
    edit_page(page_path)
else:
    open_page(page_path)
