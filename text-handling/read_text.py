#!/usr/bin/env python3


"""
Small Python Projects for Beginners
Read text from a file

Version: 1.0
Python 3.11+
Date created: November 3rd, 2023
Date modified: -
"""

FILE = "data.txt"

'''
File Mode: r = read only
Due to the use of "with", closing the file with "close()" is not necessary.
'''
with open(FILE, "r", encoding="utf-8") as text_file:
    for line in text_file:
        line = line.rstrip()
        print(line)
