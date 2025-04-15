import unittest
from unittest.mock import patch
import app  # assuming your main file is named app.py

class TestGuessGame(unittest.TestCase):

    @patch('app.input', return_value='5')
    @patch('app.random.randint', return_value=5)
    def test_user_wins(self, mock_randint, mock_input):
        result = app.result()
        self.assertEqual(result, 'You Won')

    @patch('app.input', return_value='3')
    @patch('app.random.randint', return_value=7)
    def test_user_loses(self, mock_randint, mock_input):
        result = app.result()
        self.assertIn('You Lose', result)
        self.assertIn('7', result)  # check if the hidden number is revealed

if __name__ == '__main__':
    unittest.main()
