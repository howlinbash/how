import argparse

parser = argparse.ArgumentParser(description = "Demo")
parser.add_argument("-e", "--edit", help="Edit page", action="store_true")
parser.add_argument("tag", help="Open page")

args = parser.parse_args()
