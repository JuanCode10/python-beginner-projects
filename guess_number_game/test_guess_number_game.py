# Import the unittest module and required components
import unittest
from unittest.mock import patch

# Import the functions to be tested
from guess_number_game.guess_number_game import generate_random_number, get_user_int_input, analyze_guess, parse_arguments, run_game

class TestGuessNumberGame(unittest.TestCase):

    """
    Unit tests for the Guess Number Game module.
    Tests random number generation, user input, guess analysis, argument parsing, and game loop.
    """
    #--- Test cases for generate_random_number function
    def test_easy_generate_random_number(self):
        """Test that 'easy' difficulty generates a number <= 10."""
        
        number = generate_random_number("easy")
        
        self.assertLessEqual(number, 10)

    def test_normal_generate_random_number(self):
        """Test that 'normal' difficulty generates a number <= 50."""
        
        number = generate_random_number("normal")
        
        self.assertLessEqual(number, 50)

    def test_hard_generate_random_number(self):
        """Test that 'hard' difficulty generates a number <= 100."""
        
        number = generate_random_number("hard")
        
        self.assertLessEqual(number, 100)

    def test_raise_ValueError_generate_random_number(self):
        """Test that an invalid difficulty raises ValueError."""

        with self.assertRaises(ValueError):
            generate_random_number("unknown")

    #--- Test cases for get_user_int_input function

    def test_easy_user_input(self):
        """Test user input for 'easy' difficulty returns correct integer."""
        with patch('builtins.input', return_value='7'):
            result = get_user_int_input('easy')
            self.assertEqual(result, 7)

    def test_normal_user_input(self):
        """Test user input for 'normal' difficulty returns correct integer."""
        with patch('builtins.input', return_value='42'):
            result = get_user_int_input('normal')
            self.assertEqual(result, 42)

    def test_hard_user_input(self):
        """Test user input for 'hard' difficulty returns correct integer."""
        with patch('builtins.input', return_value='100'):
            result = get_user_int_input('hard')
            self.assertEqual(result, 100)

    def test_invalid_user_input(self):
        """Test that invalid difficulty raises ValueError for user input."""
        with self.assertRaises(ValueError):
            get_user_int_input('invalid')

    # --- Test cases for analyze_guess function
    def test_analyze_guess_higher(self):
        """Test analyze_guess returns 'higher' when guess < number."""
        result = analyze_guess(5, 10)
        self.assertEqual(result, "higher")
    
    def test_analyze_guess_lower(self):
        """Test analyze_guess returns 'lower' when guess > number."""
        result = analyze_guess(15, 10)
        self.assertEqual(result, "lower")
    
    def test_analyze_guess_correct(self):
        """Test analyze_guess returns 'correct' when guess == number."""
        result = analyze_guess(10, 10)
        self.assertEqual(result, "correct")

    # --- Test cases for parse_arguments function
    def test_parse_arguments_default(self):
        """Test default argument parsing sets difficulty to 'normal'."""
        
        test_args = ['guess_number_game.py']
        with patch('sys.argv', test_args):
            args = parse_arguments()
            self.assertEqual(args.difficulty, 'normal')

    def test_parse_arguments_easy(self):
        """Test argument parsing sets difficulty to 'easy'."""
        
        test_args = ['guess_number_game.py', '--difficulty', 'easy']
        with patch('sys.argv', test_args):
            args = parse_arguments()
            self.assertEqual(args.difficulty, 'easy')

    def test_parse_arguments_hard(self):
        """Test argument parsing sets difficulty to 'hard'."""
        
        test_args = ['guess_number_game.py', '-d', 'hard']
        with patch('sys.argv', test_args):
            args = parse_arguments()
            self.assertEqual(args.difficulty, 'hard')

    def test_parse_arguments_invalid(self):
        """Test argument parsing with invalid difficulty exits the program."""
        
        test_args = ['guess_number_game.py', '--difficulty', 'invalid']
        with patch('sys.argv', test_args):
            with self.assertRaises(SystemExit):
                parse_arguments()

    # --- Test cases for run_game function
    
    def test_easy_run_game(self):
        """Test run_game for 'easy' difficulty with mocked input/output."""
        
        # Define mock input and output functions to simulate user interaction
        def mock_input(prompt):
            return '5'
        outputs = []
        
        def mock_output(message):
            outputs.append(message)
        
        # Patch the random number generator to return a fixed number
        with patch('guess_number_game.guess_number_game.generate_random_number', return_value=5):
            tries, tried_numbers = run_game('easy', input_func=mock_input, output_func=mock_output)
            self.assertEqual(tries, 1)
            self.assertEqual(tried_numbers, [5])
            self.assertIn("Selected difficulty is easy", outputs[0])
            self.assertIn("Done generating number, let's play!", outputs[1])
            self.assertIn("The number is correct", outputs[-3])
            self.assertIn("The game took 1 tries.", outputs[-1])

    def test_normal_run_game(self):
        """Test run_game for 'normal' difficulty with mocked input/output."""
        
        # Define mock input and output functions to simulate user interaction
        def mock_input(prompt):
            return '33'
        outputs = []
        
        def mock_output(message):
            outputs.append(message)
        
        # Patch the random number generator to return a fixed number
        with patch('guess_number_game.guess_number_game.generate_random_number', return_value=33):
            tries, tried_numbers = run_game('normal', input_func=mock_input, output_func=mock_output)
            self.assertEqual(tries, 1)
            self.assertEqual(tried_numbers, [33])
            self.assertIn("Selected difficulty is normal", outputs[0])
            self.assertIn("Done generating number, let's play!", outputs[1])
            self.assertIn("The number is correct", outputs[-3])
            self.assertIn("The game took 1 tries.", outputs[-1])

    def test_hard_run_game(self):
        """Test run_game for 'hard' difficulty with mocked input/output."""
        
        # Define mock input and output functions to simulate user interaction
        def mock_input(prompt):
            return '77'
        outputs = []
        
        def mock_output(message):
            outputs.append(message)
        
        # Patch the random number generator to return a fixed number
        with patch('guess_number_game.guess_number_game.generate_random_number', return_value=77):
            tries, tried_numbers = run_game('hard', input_func=mock_input, output_func=mock_output)
            self.assertEqual(tries, 1)
            self.assertEqual(tried_numbers, [77])
            self.assertIn("Selected difficulty is hard", outputs[0])
            self.assertIn("Done generating number, let's play!", outputs[1])
            self.assertIn("The number is correct", outputs[-3])
            self.assertIn("The game took 1 tries.", outputs[-1])
    
    def test_invalid_run_game(self):
        """Test run_game raises ValueError for invalid difficulty."""
        
        with self.assertRaises(ValueError):
            run_game('invalid')
