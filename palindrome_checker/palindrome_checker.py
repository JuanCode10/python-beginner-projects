#!/usr/bin/env python3

"""
This script takes a list of words provided in an input file,
verifies which of these words are palindromes, and prints them to the terminal.

Usage:
    python palindrome_checker.py <input_file>
"""

# --- Import required librarties
import sys

# --- Method Definitions

def get_input_data() -> list:
    """
    Get the data from the file provided though command line arguments.

    Returns:
        list: words imported from input file
    """    

    try:
        input_file = sys.argv[1]
        
        # read provided input file
        with open(input_file, "r") as tmp:
            input_data = [line.strip().replace(" ", "") for line in tmp if line.strip()]

    except Exception as e:
        print(f"Error reading input file:\n\t{e}")
        sys.exit(1)

    return input_data

def reverse_word_pairing (input_words: list) -> list:
    """
    Return a list of tuples containing the input word and the reversed words

    Args:
        input_words (list): Words to invert

    Returns:
        list: inverted words
    """    

    return [(word, word[::-1]) for word in input_words]

def get_palindromes(word_pairs:list) -> list:
    """
    Identify palindromes.

    Args:
        word_pairs (list): List of word, inverted_word pairs to analyze

    Returns:
        list: palindromes found
    """

    return [word for word, reversed_word in word_pairs if word == reversed_word]

def main(print_palindromes:bool=True) -> list:
    """
    Execute the main flow of the script.

    Args:
        print_palindromes (bool, optional): If True, prints found palindromes to the terminal. Defaults to True.

    Returns:
        list: List of palindromes found in the input file or provided list.
    """

    # Verify arguments were provided
    if len(sys.argv) < 2:
        print("Usage: python palindrome_checker.py <input_file>")
        sys.exit(1)

    read_words = get_input_data()

    word_pairs = reverse_word_pairing(read_words)

    palindromes = get_palindromes(word_pairs)

    # Show palindromes in terminal
    if print_palindromes:
        print("Found palindromes:")
        for word in palindromes:
            print(f"\t{word}")

    return palindromes

if __name__ == "__main__":

    main()