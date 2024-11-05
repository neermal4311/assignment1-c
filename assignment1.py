#!/usr/bin/env python3
"""
OPS445ZAA Assignment 1
Program: assignment1.py
Author: "Nirmal Gautam -ngautam11"
The python code in this file (assignment1.py) is original work written by
"Nirmal Gautam". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I am aware that infractions will be recorded and that appropriate
 action will be taken in accordance with the Academic Honesty Policy.
"""

import sys

def usage():
    """Display usage message and exit"""
    print("Usage: assignment1.py YYYY-MM-DD NN")
    sys.exit(1)
def leap_year(year):
    """Return True if the given year is a leap year, False otherwise"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
