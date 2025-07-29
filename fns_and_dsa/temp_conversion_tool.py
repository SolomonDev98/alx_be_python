#!usr/bin/env python3
# temp_conversion_tool.py
"""Objective: Illustrate the concept of variable scope by creating a script that converts temperatures between Celsius and Fahrenheit, using global variables to store conversion factors.
"""
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9

# Function that converts fahrenheit to celsuis
def convert_to_celsius(fahrenheit):
    # formula = (32°F − 32) × 5/9 = 0°C
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

# Function that converts celsuis to fahrenheit
def convert_to_fahrenheit(celsius):
    # formula = (0°C × 9/5) + 32 = 32°F
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

# Prompt user for the temperature to convert
temperature = int(input("Enter the temperature to convert: "))
celsuis_or_fahrenheit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if celsuis_or_fahrenheit == "C":
    fahrenheit = convert_to_fahrenheit(temperature)
    print(f"{temperature:.1f}°C is {fahrenheit}°F")
elif celsuis_or_fahrenheit == "F":
    celsius = convert_to_celsius(100)
    print(f"{temperature:.1f}°F is {celsius}°C")
else:
    print("Invalid Temperature. Please enter a numeric value.")

    