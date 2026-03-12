#!/usr/bin/python3
import sys

def factorial(n):
    if n < 0: return "Error"
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# We use sys.argv[1:] to skip the script name itself
for arg in sys.argv[1:]:
    try:
        num = int(arg)
        print(f"Factorial of {num} is {factorial(num)}")
    except ValueError:
        print(f"'{arg}' is not a valid number, skipping.")