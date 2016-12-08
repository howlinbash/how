#! /usr/bin/python3

import argparse, subprocess

manual_path = "/home/howlin/src/manual/"

docker = 'tools/docker.md'
git    = 'tools/git.md'
vim    = 'tools/vim.md'

tags = {'docker': docker, 'git': git, 'vim': vim}

def open_page(page_path):
    url = "file:///" + manual_path + page_path
    subprocess.call(['chromium', url])

def edit_page(page_path):
    command = manual_path + page_path
    subprocess.call(['vim', command])

parser = argparse.ArgumentParser(description = "Demo")
parser.add_argument("-e", "--edit", help="Edit page", action="store_true")
parser.add_argument("tag", help="Open page")
args = parser.parse_args()

tag = args.tag

page_path = str(tags.get(tag, 0))

if args.edit:
    edit_page(page_path)
else:
    open_page(page_path)
