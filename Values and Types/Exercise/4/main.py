#!/usr/bin/env python3

"""

Write a program which prompts the user for a Celsius temperature, convert the temperature to Fahrenheit, and print out the converted temperature.

"""

#
celcius = input("Enter Temperature in Celcius: ")
celcius = float(celcius)

# (0°C × 9/5) + 32 = 32°F
fahrenheit = float(celcius * (9/5) + 32)

#
print("\n")
print("Celcius: %.2f" % celcius)
print("Fahrenheit: %.2f" % fahrenheit)
