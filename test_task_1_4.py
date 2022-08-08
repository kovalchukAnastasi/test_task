import unittest
from task_1 import reversed_text

class Test_reversed_text(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_small_text(self):
        text = 'The quick brown fox'
        result = reversed_text(text)
        self.assertEqual(result, 'fox brown quick The')
    
if __name__ == '__main__':
    unittest.main()
