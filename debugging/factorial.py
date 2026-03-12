#!/usr/bin/python3
import sys

def factorial(n):
    # Factorial is not defined for negative numbers
    if n < 0:
        return "Error: Negative input"
    
    result = 1
    while n > 1:
        result *= n
        n -= 1  # Decrement n to eventually exit the loop
    return result

# Basic error handling for command line arguments
if len(sys.argv) > 1:
    try:
        num = int(sys.argv[1])
        print(factorial(num))
    except ValueError:
        print("Please provide a valid integer.")
else:
    print("Usage: ./script.py <number>")