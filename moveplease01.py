#!/usr/bin/env python3

# Shell library imports
import shutil # Shell utilties will be used to move files
import os # Allow access to low level OS operations

def main():

    # Ensures the script starts in this directory.
    os.chdir('/home/student/mycode')

    # Move Raynor to ceph_storage.
    shutil.move('raynor.obj', 'ceph_storage/')

    # Rename Raynor's girlfriend since they broke up.
    xname = input('What is the new name for kerrigan.obj? ')

    # Move Raynor's girlfiend with him. 
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()