"""
Implementing a basic interface.
"""

## This file is available from https://github.com/adbar/trafilatura_gui
## under GNU GPL v3 license

import sys

from gooey import Gooey
from trafilatura.cli import map_args, parse_args, process_args



@Gooey
def main():
    """ Run as a command-line utility. """
    args = parse_args(sys.argv[1:])
    args = map_args(args)
    process_args(args)


if __name__ == '__main__':
    main()

