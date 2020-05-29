#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
import urllib.parse
import signal

sArgParser=argparse.ArgumentParser(add_help=False, description="URL encode or decode input from standard input.")
sArgParser.add_argument('-d', '--decode', help='Decode input from standard input.', action="store_true")
sArgParser.add_argument('-e', '--encode', help='Encode input from standard input.', action="store_true")
aArguments=sArgParser.parse_args()

def SignalHandler(sig, frame):
    # Create a break routine:
    sys.stderr.write("\nCtrl-C detected, exiting...\n")
    sys.exit(1)

signal.signal(signal.SIGINT, SignalHandler)

try:    # skip if binary values are given
    strTotalInput = []
    for strInput in sys.stdin:
        strTotalInput.append(strInput)
except UnicodeError:
    pass

for sInput in strTotalInput:
    sInput = sInput.strip()
    if aArguments.decode:
        print(urllib.parse.unquote(sInput))
    elif aArguments.encode:
        print(urllib.parse.quote(sInput).strip())
    else:
        sys.stderr.write("Please use -d/--decode or -e/--encode.\n\n")
        sys.exit(2)