#!/usr/bin/env python3
# arithmetic_operations.py
"""Define a Function that performs basic arithmetic operations"""

# function definition for arithmetic operations(add, subtract, multiply, divide)
def perform_operation(num1, num2, operation):
    match operation:
        case "add":
            return num1 + num2
        case "subtract":
            return num1 - num2
        case "multiply":
            return num1 * num2
        case "divide":
            if num2 == 0:
                return "Error!, you denominator can not be 0"
            elif num2 != 0:
                return num1 / num2
        case _:
            return "Invalid input, please try again"