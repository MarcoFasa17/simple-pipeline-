import unittest
from app import count_vowels
class TestApp(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels("hello"), 2)
if __name__ == "__main__":
    unittest.main()