#!/usr/bin/env python3

"""
Simple CLI Calculator
---------------------
A command-line calculator that supports basic arithmetic operations
(add, subtract, multiply, divide, power, square root, cube root).
Keeps a history of calculations and handles invalid input gracefully.
"""

# Import required libraries
from math import sqrt, pow, cbrt
import inspect

def add(a: float, b: float) -> float:
    """Return the sum of two numbers.

    Args:
        a (float): The first addend
        b (float): The second addend

    Returns:
        float: The result of a + b
    """    
    return a + b

def subtract(a: float, b: float) -> float:
    """Return the difference of two numbers.

    Args:
        a (float): The minuend (number to subtract from)
        b (float): The subtraend (number to subtract)

    Returns:
        float: The result of a - b
    """    
    return a - b

def multiply(a: float, b: float) -> float:
    """Return the product of two numbers.

    Args:
        a (float): The first number for multiplication
        b (float): The second number for multiplication

    Returns:
        float: The result of a * b
    """    
    return a * b

def divide(a: float, b: float) -> float:
    """Return the division of two numbers.

    Args:
        a (float): The dividend (number to be divided)
        b (float): The divisor (number to divide by)

    Returns:
        float: The result of a / b
    """
    return a/b

def power(a: float, b: float) -> float:
    """Return the result of raising a base number to an exponent.

    Args:
        a (float): The base number
        b (float): The exponent

    Returns:
        float: The value of a raised to the power of b
    """    
    return pow(a, b)

def square_root(a: float) -> float:
    """Return the square root of a given number.

    Args:
        a (float): The number to calculate the square root of

    Returns:
        float: The result of sqrt(a)
    """    
    return sqrt(a)

def cube_root(a: float) -> float:
    """Return the cube root of a given number.

    Args:
        a (float): The number to calculate the cube root of

    Returns:
        float: The result of cbrt(a)
    """    
    return cbrt(a)

def show_history(history: list[str]) -> None:
    """Print on terminal all the operations performed so far.

    Args:
        history (list[str]): A list of operations and their results put together in strings
    """    

    print("All operations performed so far:")
    
    for item in history:
        print(f"\t{item}")

def calculator() -> None:
    """Execute the calculator script flow.
    """
    print("Welcome to the CLI Calculator script.")
    
    # --- Declare useful variables
    operation_map = {
        "1": add,
        "2": subtract,
        "3": multiply,
        "4": divide,
        "5": power,
        "6": square_root,
        "7": cube_root,
        "8": show_history,
        "0": "exit"
    }
    operation_history = []
    operation = None

    # --- Execute while loop to run all the calculations
    while operation != "exit":
        
        # Choice menu
        print("\n===========================================================================")
        print("Please choose one of the following operations:")
        print("1. Add")
        print("2. Difference")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square root")
        print("7. Cube root")
        print("8. Show operation history")
        print("0. Exit")
        
        # Get user input
        user_input = input("Please type your choice number and press enter: ")

        # Validate user input
        if user_input not in operation_map.keys():
            print(f"'{user_input}' is not a valid option, please try again.")
            continue

        operation = operation_map[user_input]

        # Handling of special input cases
        if user_input == "0":
            continue # let this reach the next execution to test while loop definition
        
        if user_input == "8":
            operation(operation_history)
            continue

        # Regular operation execution algorithm
        try:
            args = [float(input(f"\nEnter number {i+1}: ")) for i in range(len(inspect.signature(operation).parameters))]
        except Exception as e:
            print(f"\n\nError:\n\t{e}\n")
            input("Press enter to get back to operation selection")
            continue

        # Calculate operation result
        try:
            result = operation(*args)
        except Exception as op_error:
            print(f"Error executing operation:\n\t{op_error}")
            continue

        # Print the adequate msg depending on the operation performed
        match user_input:
            case "1":
                msg = f"{args[0]} + {args[1]} = {result}"
                
            case "2":
                msg = f"{args[0]} - {args[1]} = {result}"
                
            case "3":
                msg = f"{args[0]} * {args[1]} = {result}"
                
            case "4":
                msg = f"{args[0]} / {args[1]} = {result}"
                
            case "5":
                msg = f"pow({args[0]}, {args[1]}) = {result}"
                
            case "6":
                msg = f"sqrt({args[0]}) = {result}"
                
            case "7":
                msg = f"cbrt({args[0]}) = {result}"
                
        print(f"\n{msg}")

        # Add operation string to history
        operation_history.append(msg)


if __name__ == "__main__":

    calculator()