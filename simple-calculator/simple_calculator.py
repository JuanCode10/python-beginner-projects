#!/usr/bin/env python3

# Import required libraries
from math import *
import inspect

def sum (a:int, b:int) -> int:
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    return a/b

def power (a, b):
    return pow(a, b)

def square_root (a):
    return sqrt(a)

def cube_root (a):
    return cbrt(a)

def show_history (history):

    print("All operations performed so far:")
    
    for item in history:
        print(f"\n\t {item}")

def calculator():

    print("Welcome to the CLI Calculator script.")
    
    operation_map = {
        "1": sum,
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
    operation= None

    while operation != "exit":
        
        print("\n===========================================================================")
        print("Please choose one of the following operations:")
        print("1. Sum")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Square root")
        print("7. Cube root")
        print("8. Show operation history")
        print("0. Exit")
        
        user_input = input("Please type your choice number and press enter: ")

        if user_input not in operation_map.keys():
            print(f"'{user_input}' is not a valid option, please try again.")
            continue

        operation = operation_map[user_input]

        if user_input == "0":
            continue # let this reach the next execusion to test while loop definition
        
        if user_input == "8":
            operation(operation_history)
            continue

        # Get the reuquired arguments to run the method:
        try:
            args = [float(input("\nType a number for the operation: ")) for _ in range(len(inspect.signature(operation).parameters))]
        except Exception as e:
            print(f"\n\nError:\n\t{e}\n")
            input("Press enter to get back to operation selection")

        # Calculate operation result
        result = operation(*args)

        # print the adequate msg depeding on the operation performed
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
                msg = f"pwr({args[0]}, {args[1]}) = {result}"
                
            case "6":
                msg = f"sqrt({args[0]}) = {result}"
                
            case "7":
                msg = f"cbrt({args[0]}) = {result}"
                
        print(f"\n{msg}")
        operation_history.append(msg)


if __name__ == "__main__":

    calculator()