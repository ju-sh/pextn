__version__ = "0.1"
__author__ = "Julin"

import argparse

from pextn import pextn, UnknownExtension

parser = argparse.ArgumentParser(
    prog="pextn",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    description="A simple, lazy utility to display information about a file extension"
)
parser.add_argument(
    '--version',
    action='version',
    version='%(prog)s ' + __version__
)
parser.add_argument("extension", help="Extension")
args = parser.parse_args()

try:
    extn_info_lists = pextn(args.extension)
    print(f"Extension: {args.extension}")
    print("-" * (len("Extension: ") + len(args.extension)))
    for info_list in extn_info_lists:
        print(f"{info_list[0]}")
        if info_list[1]:
            print(f"Used by: {info_list[1]}")
        print()
except UnknownExtension:
    print(f"Not sure what '{args.extension}' is...")
