# 🐍 Beginner Python Scripts

A collection of small, beginner-friendly Python projects. Each project lives in its own directory and demonstrates fundamental programming concepts such as functions, loops, conditionals, error handling, and working with the Python standard library.

---

## 🚀 Getting Started

Clone this repository:

```bash
git clone https://github.com/JuanCode10/python-beginner-projects.git
cd python-beginner-projects
```

Make sure you have Python 3.12.0 or higher installed.  
To run any project, navigate into its directory and follow the usage instructions below.

---

## Requirements

- Python 3.12.0 or higher

---

## 📦 Dependencies

All scripts use only Python's standard library.  
No external dependencies are required.

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

---

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

Where `sample.txt` is a text file containing one word per line.

---

### 3. Guess the Number Game (`guess_number_game/`)

A command-line game where you try to guess a randomly generated number based on the selected difficulty:

- Difficulty levels: easy (0-10), normal (0-50), hard (0-100)
- The game provides feedback after each guess: "higher", "lower", or "correct"
- Tracks all your guesses and the number of attempts
- Handles invalid input gracefully

Run it:

```bash
cd guess_number_game
python3 guess_number_game.py --difficulty easy
```

You can also use `--difficulty normal` or `--difficulty hard` (default is normal).  
The game will prompt you to guess until you find the correct number.

---

## 🧪 Running Unit Tests

This project includes unit tests for each script. To run all unit tests across the project, use Python's unittest discovery feature:

```bash
python3 -m unittest discover
```

This command will automatically find and run all test files named `test*.py` in any subdirectory.  
Make sure your test files follow this naming convention.

---

## 📜 License

This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

---

## 👤 Author

**JuanCode10**  
[GitHub Profile](https://github.com/JuanCode10)

---

## 🤝 Contributing

Contributions, suggestions, and feedback are welcome!  
Feel free to open issues or pull requests to improve these beginner projects.

---
