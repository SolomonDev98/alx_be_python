#!/usr/bin/env python3
# Simple Calculator with Match Case

# Collect operands from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# collect operator from user
operator = input("Choose the operation (+, -, *, /): ")

# Perform the Calculation Using Match Case:

match operator:
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            print("Error: Zero Divison!.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")