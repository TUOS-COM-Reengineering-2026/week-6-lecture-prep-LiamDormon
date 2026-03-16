import unittest
from prep import strange_function

class MyTestCase(unittest.TestCase):
    test_cases = [
        (1, 1, 2, 3, 'behaviour 1'),
        (1, 1, 3, 2, 'behaviour 2'),
        (1, 2, 3, 4, 'behaviour 3'),
        (3, 2, 1, 0, 'behaviour 4'),
        (3, 2, 1, 4, 'behaviour 5'),
        (4, 2, 4, 3, 'behaviour 6'),
    ]

    def test_strange_function(self):
        for a, b, c, d, expected in self.test_cases:
            with self.subTest(a=a, b=b, c=c, d=d):
                self.assertEqual(strange_function(a, b, c, d), expected)

    