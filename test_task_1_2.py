import unittest
from task_1 import shortest_sent_and_num_of_words

class Test_shortest_sent_and_num_of_words(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_small_text(self):
        text = 'One. Two two. Three three three.'
        result = shortest_sent_and_num_of_words(text)
        self.assertEqual(result, [('One', 1)])
    
if __name__ == '__main__':
    unittest.main()
