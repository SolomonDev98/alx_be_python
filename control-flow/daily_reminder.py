#!/usr/bin/env python3
# Personal Daily Reminder

# Prompt user for task, priority and time_bound input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time_bound? (yes/no): ").lower()

# Process the Task Based on Priority and Time Sensitivity

match priority:
    case "high":
        if time_bound == "yes":
            print(f"{task} is a high priority task that requires immediate attention today!")
        else:
            print(f"{task} is a high a high priority task, endeavor to finish it." )
    case "medium":
        if time_bound == "yes":
            print(f"{task} is a medium priority task that requires attention.")
        else:
            print(f"task is a medium priority task, Try to complete it")
    case "low":
        print(f"{task} is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Watch out for spelling errors when filling the priority and time bound field. Try again!")
