#!/usr/bin/env python3

"""

Write a program to prompt the user for hours and rate per hour to compute gross pay.


Enter Hours: 35
Enter Rate: 2.75
Pay: 96.25

"""

# Ask user input; Hours
hours = input("Enter Hours: ")
hours = float(hours)

# Ask user input; Rate
rate = input("Enter Rate: ")
rate = float(rate)

# Pay calculation
pay = hours * rate

#
print(pay)
