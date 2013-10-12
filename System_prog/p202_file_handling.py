#!/usr/bin/env python

# This module explains file handling (creation, renaming deletion) in python.

import os

# Rename file
os.rename("new_file.txt", "renamed.txt")

# Delete file
os.remove("renamed.txt")

# Create new directory
os.mkdir("new folder")

# Get current working dir
print os.getcwd()

# we can also use methods like os.rmdir(), os.chdir() to remove and change dirs
