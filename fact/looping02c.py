#!/usr/bin/env python3
"""TLG Learning | AAlegre
   For - Looping across a file opened with 'with'
         while also being gentle on memory consumption."""

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    
    # loop over lines
    for svr in dnsfile:
        #print and end without a newline
        print(svr, end="")

# no need to close our file - closed automatically
