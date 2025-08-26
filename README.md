# 🐍 Beginner Python Scripts

A collection of small, beginner-friendly Python projects. Each project lives in its own directory and demonstrates fundamental programming concepts such as functions, loops, conditionals, error handling, and working with the Python standard library.

---

## 📂 Project List

### 1. CLI Calculator (`simple_calculator/`)

A command-line calculator that supports basic arithmetic operations:

- Add, subtract, multiply, divide
- Power, square root, cube root
- Keeps a history of all operations performed
- Handles invalid input gracefully

Run it:

```bash
cd simple_calculator
python3 simple_calculator.py
```

### 2. Palindrome Checker (`palindrome_checker/`)

This script takes a list of words from an input file, checks which ones are palindromes, and prints them to the terminal.

- Reads words from a text file provided as a command-line argument
- Cleans up whitespace and ignores empty lines
- Identifies and lists all palindromes found

Run it:

```bash
cd palindrome_checker
python3 palindrome_checker.py sample.txt
```

Where sample.txt is a text file containning one word per line.

---

## 🧪 Running Unit Tests

This project includes unit tests for each script. To run all unit tests across the project, use Python's unittest discovery feature:

```bash
python3 -m unittest discover
```

This command will automatically find and run all test files named `test*.py` in any subdirectory. Make sure your test files follow this naming convention.
