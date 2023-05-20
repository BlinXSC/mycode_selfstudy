#!/usr/bin/env python3
"""TLG Learning | AAlegre
    For - Looping across a file opened with 'with"""

# Open file in read mode
with open("dnsservers.txt", "r") as dnsfile:

    # Indent to keep the dnsfile object open
    # Create list of lines
    dnslist = dnsfile.readlines()

    # Loop over lines
    for svr in dnslist:
        # Print and end without a newline
        print(svr, end = "") # The line we read already has a newline (\n)
