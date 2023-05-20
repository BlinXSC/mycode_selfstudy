#!/usr/bin/env python3
"""TLG Learning | AAlegre
    For - Using a file's lines as a source for the for-loop"""

# Open file in read mode
dnsfile = open("dnsservers.txt", "r")

# Create list of lines
dnslist = dnsfile.readlines()

# Loop over lines
for svr in dnslist:
    # Print and end without a newline
    print(svr, end = "") # The line we read already has a newline (\n)

# Close the file (we created the list of lines)
    dnsfile.close() # Best practice to close your file

