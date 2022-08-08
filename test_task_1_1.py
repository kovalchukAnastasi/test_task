import unittest
from task_1 import top_3_words

class Test_top_3_words(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_small_text(self):
        text = 'a a a a b b b c c d e f g'
        result = top_3_words(text)
        self.assertEqual(result, [('a', 4), ('b', 3), ('c', 2)])
    def test_bigger_text(self):
        text = 'one, two two! three three three; four: four four four?/'
        result = top_3_words(text)
        self.assertEqual(result, [('four', 4), ('three', 3), ('two', 2)])

if __name__ == '__main__':
    unittest.main()
