#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0: return "undefined (negative)"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Iterate directly over the slice
for arg in sys.argv[1:]:
    if arg.isdigit():
        num = int(arg)
        print(f"Factorial of {num} is {factorial(num)}")
    else:
        print(f"Skipping '{arg}': Not a positive integer")