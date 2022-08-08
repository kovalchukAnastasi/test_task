import unittest
from task_2 import Cell, check_map

class Test_check_map(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_no_trees(self):
        el_00 = Cell(False, [0, 0], False)
        el_01 = Cell(False, [0, 1], False)
        el_10 = Cell(False, [1, 0], False)
        el_11 = Cell(False, [1, 1], False)
        map = [[el_00, el_01],
               [el_10, el_11]]
        result = check_map(map)
        self.assertEqual(result, [])
    def test_four_trees(self):
        el_00 = Cell(True, [0, 0], False)
        el_01 = Cell(True, [0, 1], False)
        el_02 = Cell(False, [0, 2], False)
        el_03 = Cell(True, [0, 3], False)
        el_10 = Cell(False, [1, 0], False)
        el_11 = Cell(False, [1, 1], False)
        el_12 = Cell(False, [1, 2], False)
        el_13 = Cell(False, [1, 3], False)
        el_20 = Cell(True, [2, 0], False)
        el_21 = Cell(False, [2, 1], False)
        el_22 = Cell(False, [2, 2], False)
        el_23 = Cell(False, [2, 3], False)
        el_30 = Cell(False, [3, 0], False)
        el_31 = Cell(False, [3, 1], False)
        el_32 = Cell(True, [3, 2], False)
        el_33 = Cell(True, [3, 3], False)
        map = [[el_00, el_01, el_02, el_03],
               [el_10, el_11, el_12, el_13], 
               [el_20, el_21, el_22, el_23],
               [el_30, el_31, el_32, el_33]]
        result = check_map(map)
        self.assertEqual(result, [[[0, 0], [0, 1]], [[0, 3]], [[2, 0]], [[3, 2], [3, 3]]])

if __name__ == '__main__':
    unittest.main()