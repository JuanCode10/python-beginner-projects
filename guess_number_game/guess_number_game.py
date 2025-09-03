#!/usr/bin/env python3

"""
Guess the Number Game
---------------------
This module implements a simple number guessing game with multiple difficulty levels.
It includes functions for generating random numbers, handling user input, analyzing guesses,
parsing command-line arguments, and running the game loop.
"""

# --- Import python libraries

import random
import argparse

# --- Useful global variables

difficulty_interval_map = {
        "easy"  : (0, 10 ),
        "normal": (0, 50 ),
        "hard"  : (0, 100)
    }

# --- Method definitons


def generate_random_number(difficulty: str) -> int:
    """
    Generate a random number based on the difficulty level.

    Args:
        difficulty (str): The difficulty level ('easy', 'normal', 'hard').

    Returns:
        int: Random number within the difficulty interval.

    Raises:
        ValueError: If an invalid difficulty is provided.
    """
    match difficulty:
        case "easy":
            return random.randint(0, 10)
        case "normal":
            return random.randint(0, 50)
        case "hard":
            return random.randint(0, 100)
        case _:
            raise ValueError("Invalid difficulty provided. Please choose: 'easy', 'normal', or 'hard'")

def get_user_int_input(difficulty: str) -> int:
    """
    Prompt the user for an integer input within the difficulty interval.

    Args:
        difficulty (str): The difficulty level.

    Returns:
        int: The user's valid integer input.

    Raises:
        ValueError: If an invalid difficulty is provided.
    """
    if difficulty not in difficulty_interval_map:
        raise ValueError("Invalid difficulty level")

    low, high = difficulty_interval_map[difficulty]

    while True:
        try:
            number = int(input(f"Please provide a number between {low} and {high}: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue

        if low <= number <= high:
            return number
        else:
            print(f"Please provide a number between {low} and {high}.")

def analyze_guess(guess: int, number: int) -> str:
    """
    Analyze the user's guess compared to the target number.

    Args:
        guess (int): The user's guess.
        number (int): The target number.

    Returns:
        str: 'higher', 'lower', or 'correct'.
    """
    if guess < number:
        return "higher"
    elif guess > number:
        return "lower"
    else:
        return "correct"

def parse_arguments():
    """
    Parse command-line arguments for the game.

    Returns:
        Namespace: Parsed arguments with difficulty setting.
    """
    parser = argparse.ArgumentParser(description="Guess the Number Game")
    parser.add_argument(
        "-d", "--difficulty",
        choices=["easy", "normal", "hard"],
        default="normal",
        help="Set the game difficulty level (default: normal)"
    )
    return parser.parse_args()

def run_game(difficulty_setting: str, input_func=input, output_func=print):
    """
    Run the main game loop for the guessing game.

    Args:
        difficulty_setting (str): The difficulty level.
        input_func (callable): Function to get user input (default: input).
        output_func (callable): Function to output messages (default: print).

    Returns:
        tuple: (number of tries, list of tried numbers)
    """
    output_func(f"Selected difficulty is {difficulty_setting}")

    # Generate the target number
    number = generate_random_number(difficulty_setting)

    output_func("Done generating number, let's play!")

    guess = -1
    tries = 0
    tried_numbers = []

    # Main game loop
    while guess != number:
        try:
            guess = int(input_func(
                f"Please provide a number between {difficulty_interval_map[difficulty_setting][0]} "
                f"and {difficulty_interval_map[difficulty_setting][1]}: "
            ))
        except ValueError:
            output_func("Invalid input! Please enter an integer.")
            continue

        # Track and sort all guesses
        tried_numbers.append(guess)
        tried_numbers.sort()

        tries += 1

        # Analyze guess and provide feedback
        status = analyze_guess(guess, number)
        output_func(f"The number is {status}")
        output_func(f"You have tried the following numbers: {tried_numbers}\n")

    output_func(f"The game took {tries} tries.")
    return tries, tried_numbers

if __name__ == "__main__":
    args = parse_arguments()
    run_game(args.difficulty)