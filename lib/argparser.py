import argparse

parser = argparse.ArgumentParser(description = "Demo")
group = parser.add_mutually_exclusive_group()

group.add_argument(
        "-c", 
        "--print-contents", 
        help="Print directory tree of manual pages", 
        action="store_true"
)

group.add_argument(
        "-l", 
        "--list-tags", 
        help="List all tags and page paths", 
        action="store_true"
)

parser.add_argument(
        "-v", 
        "--view", 
        help="View page", 
        nargs='+'
)

parser.add_argument(
        "tag", 
        nargs='?',
        help="Open page"
)

args = parser.parse_args()
