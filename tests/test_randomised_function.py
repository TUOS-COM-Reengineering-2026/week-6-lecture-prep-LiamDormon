import unittest
from unittest.mock import patch
from lecture import randomised_function

class MyTestCase(unittest.TestCase):

    @patch('random.randint')
    def test_randomised_function_low(self, mock_randint):
        mock_randint.return_value = 3

        self.assertEqual('software', randomised_function()) 

    @patch('random.randint')
    def test_randomised_function_high(self, mock_randint):
        mock_randint.return_value = 7

        self.assertEqual('engineering', randomised_function())
