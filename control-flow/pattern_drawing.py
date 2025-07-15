#!/usr/bin/env python3
# Drawing Patterns with Nested Loops

# Prompt User for Pattern size

size = int(input("Enter the size of the pattern: "))
count = 0

# outer loop
while (size != count):
    # inner loop
    for j in range(size):
        print("*", end="")
    count += 1
    print()