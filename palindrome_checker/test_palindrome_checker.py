# --- Import required python libraries
import unittest
from   unittest import mock
import tempfile
import os

# --- Import the functions to be tested
from palindrome_checker.palindrome_checker import get_input_data, reverse_word_pairing, get_palindromes, main

class TestPalindromeChecker(unittest.TestCase):
    """
    Unit tests for the palindrome_checker module functions.
    Tests file reading, word reversal, and palindrome detection logic.
    """

    def test_get_input_data_file(self):
        """
        Test that get_input_data reads words correctly from a file.
        """
        
        # Create a temporary file with sample data
        with tempfile.NamedTemporaryFile(mode="w+t", delete=False) as tmpfile:
            tmpfile.write("racecar\nhello\nlevel\nworld\n")
            tmpfile_name = tmpfile.name
        
        # Patch sys.argv to simulate command line input
        with mock.patch("sys.argv", ["palindrome_checker.py", tmpfile_name]):
            result = get_input_data()
            self.assertEqual(result, ["racecar", "hello", "level", "world"])
        
        # Clean up the temporary file
        os.remove(tmpfile_name)

    def test_get_input_data_file_strips_spaces(self):
        """
        Test that get_input_data strips spaces from lines when reading from a file.
        """

        # Create a temporary file with lines containing spaces
        with tempfile.NamedTemporaryFile(mode="w+t", delete=False) as tmpfile:
            tmpfile.write(" racecar  \n  hello\nlevel   \n   world\n\n")
            tmpfile_name = tmpfile.name
        
        # Patch sys.argv to simulate command line input
        with mock.patch("sys.argv", ["palindrome_checker.py", tmpfile_name]):
            result = get_input_data()
            self.assertEqual(result, ["racecar", "hello", "level", "world"])

        # Clean up the temporary file
        os.remove(tmpfile_name)

    def test_reverse_word_pairing(self):
        """
        Test that reverse_word_pairing returns correct word and reversed word pairs.
        """
        
        input_words = ["racecar", "hello", "level"]
        expected_output = [("racecar", "racecar"), ("hello", "olleh"), ("level", "level")]
        result = reverse_word_pairing(input_words)
        self.assertEqual(result, expected_output)

    def test_get_palindromes(self):
        """
        Test that get_palindromes returns only words that are palindromes.
        """
        
        word_pairs = [("racecar", "racecar"), ("hello", "olleh"), ("level", "level"), ("world", "dlrow")]
        expected_output = ["racecar", "level"]
        result = get_palindromes(word_pairs)
        self.assertEqual(result, expected_output)

    def test_main_flow(self):
        # Create a temporary file with sample data
        with tempfile.NamedTemporaryFile(mode="w+t", delete=False) as tmpfile:
            tmpfile.write("racecar\nhello\nlevel\nworld\n")
            tmpfile_name = tmpfile.name
        
        # Patch sys.argv to simulate command line input
        with mock.patch("sys.argv", ["palindrome_checker.py", tmpfile_name]):
            result = main(print_palindromes=False)
            self.assertEqual(result, ["racecar", "level"])

        # Clean up the temporary file
        os.remove(tmpfile_name)