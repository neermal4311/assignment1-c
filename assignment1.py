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
    """This shows whether the given year is leap year or no"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def mon_max(month, year):
    """ This gives the max number of days in the given month and year"""
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year(year) else 28
    else:
        return 31

def valid_date(date):
    """Check if the given date is valid"""
    try:
        day, month, year = map(int, date.split('/'))
        if year < 1 or month < 1 or month > 12 or day < 1:
            return False
        return day <= mon_max(month, year)
    except ValueError:
        return False

def day_of_week(date):
    """Return the day of the week for the given date"""
    day, month, year = map(int, date.split('/'))
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    h = (day + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) - (2 * j)) % 7
    days = ['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri']
    return days[h]
def after(date):
    """Return the date after the given date"""
    day, month, year = map(int, date.split('/'))
    day += 1
    if day > mon_max(month, year):
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    return f"{day:02d}/{month:02d}/{year:04d}"

def before(date):
    """Return the date before the given date"""
    day, month, year = map(int, date.split('/'))
    day -= 1
    if day < 1:
        month -= 1
        if month < 1:
            month = 12
            year -= 1
        day = mon_max(month, year)
    return f"{day:02d}/{month:02d}/{year:04d}"

def day_iter(start_date, num_days):
    """Return the end date after iterating through the given number of days"""
    date = start_date
    for _ in range(abs(num_days)):
        date = after(date) if num_days > 0 else before(date)
    return date
if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
    
    start_date = sys.argv[1]
    try:
        num_days = int(sys.argv[2])
    except ValueError:
        usage()
    
    if not valid_date(start_date):
        usage()
    
    end_date = day_iter(start_date, num_days)
    day = day_of_week(end_date)
    
    print(f"The end date is {day}, {end_date}.")
