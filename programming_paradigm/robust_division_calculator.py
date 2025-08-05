#!/usr/bin/env python3
# robust_division_calculator.py
"""
Objective: Implement a division calculator that robustly handles errors like division by zero and non-numeric inputs using command line arguments.
"""

def safe_divide(numerator, denominator):
    # Function that performs divsion and handles zero_division_error
    try:
        result = float(numerator) / float(denominator)
    except ZeroDivisionError as e:
        return "Error: Cannot divide by zero."
    except ValueError as e:
        return "Error: Please enter numeric values only."
    else:
        return f"The result of the division is {result}"