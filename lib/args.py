#!/usr/bin/env python3

import argparse
from lib.banner import __version__

parser = argparse.ArgumentParser(description="Advanced information gathering toolkit for phone numbers.",
                                 usage='%(prog)s -n <number> [options]')

parser.add_argument('-n', '--number', metavar='number', type=str,
                    help='The phone number to scan (E164 or international format)')

parser.add_argument('-i', '--input', metavar="input_file", type=argparse.FileType('r'),
                    help='Phone number list to scan (one per line)')

parser.add_argument('-o', '--output', metavar="output_file", type=argparse.FileType('w'),
                    help='Output to save scan results')

parser.add_argument('-s', '--scanner', metavar="scanner", default="all", type=str,
                    help='The scanner to use')

parser.add_argument('--recon', action='store_true',
                    help='Launch custom format reconnaissance')

parser.add_argument('--no-ansi', action='store_true',
                    help='Disable colored output')

parser.add_argument('-v', '--version', action='store_true',
                    help='Show Phonia Toolkit version')

parser.add_argument('-u', '--update', action='store_true',
                    help='Update Phonia Toolkit')

args = parser.parse_args()
