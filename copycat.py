#!/usr/bin/env python3

# Imports additional code to manipulate our files and directories.
import shutil
import os

def main():

    # Move into the working directory
    os.chdir("/home/student/mycode/")

    # Copy fileA to fileB
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    # Copy directoryA to directoryB, creating a directory if it doesn't already exist.
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

# Call the main function
if __name__ == "__main__":
    main()