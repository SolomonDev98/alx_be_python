#!/usr/bin/env python3
# Drawing Patterns with Nested Loops

# Prompt User for Pattern size

size = int(input("Enter the size of the pattern: "))

# outer loop
for i in range(size):
    # inner loop
    for j in range(size):
        print("*", end="")
    print()