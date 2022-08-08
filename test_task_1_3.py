import unittest
from task_1 import capitalized_through_one

class Test_capitalized_through_one(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_small_text(self):
        text = 'The quick brown fox'
        result = capitalized_through_one(text)
        self.assertEqual(result, 'ThE QuIcK BrOwN FoX')
    
if __name__ == '__main__':
    unittest.main()
