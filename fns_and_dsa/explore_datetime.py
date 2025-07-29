#!/usr/bin/env python3
# explore_datetime.py
from datetime import datetime, timedelta

# Display current date and time
def display_current_datetime():
    return datetime.now()

current_date = display_current_datetime()
print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

# Calculate a future date
number_of_days = int(input("Enter the number of days to add to the current date: "))

def calculate_future_date():
    return timedelta(days=number_of_days)

future_date = current_date + calculate_future_date()
print(f"Future date:{future_date.strftime('%Y-%m-%d')}")