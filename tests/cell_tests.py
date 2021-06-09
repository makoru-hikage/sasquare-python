from functools import partial

import unittest

from single_array_square.parts import *
from single_array_square.selections import *

class TestCellFunctions(unittest.TestCase):

    ## Test the all the pairs of row and column indices
    ## on the Intersection Function
    def test_intersection_function_of_b5 (self):
        cell_indices = []
        base = 5
        line_indices = range (1, base + 1)
        for r in line_indices:
            for c in line_indices:
                cell_indices.append(
                    get_intersection_index(base, r, c)
                )
        supposed_cell_indices = list(range (1, base*base + 1))
        self.assertEqual(cell_indices, supposed_cell_indices)

    def test_all_row_cells_of_b5 (self):
        base = 5
        line_indices = range (1, base + 1)
        row1 = (1,2,3,4,5)
        row2 = (6,7,8,9,10)
        row3 = (11,12,13,14,15)
        row4 = (16,17,18,19,20)
        row5 = (21,22,23,24,25)
        supposed_all_rows = [row1, row2, row3, row4, row5]
        all_rows = map (partial(select_row,base), line_indices)
        self.assertEqual(list(all_rows), supposed_all_rows)

    def test_all_col_cells_of_b5 (self):
        base = 5
        line_indices = range (1, base + 1)
        column1 = (1,6,11,16,21)
        column2 = (2,7,12,17,22)
        column3 = (3,8,13,18,23)
        column4 = (4,9,14,19,24)
        column5 = (5,10,15,20,25)
        supposed_all_columns = [
            column1,
            column2,
            column3,
            column4,
            column5
        ]
        all_columns = map (partial(select_column,base), line_indices)
        self.assertEqual(list(all_columns), supposed_all_columns)

    def test_rowcol_pairs_of_b5 (self):
        base = 5
        supposed_pairs = [
            (1,1), (1,2), (1,3), (1,4), (1,5),
            (2,1), (2,2), (2,3), (2,4), (2,5),
            (3,1), (3,2), (3,3), (3,4), (3,5),
            (4,1), (4,2), (4,3), (4,4), (4,5),
            (5,1), (5,2), (5,3), (5,4), (5,5)
        ]

        cell_indices = range(1,base*base + 1)
        all_pairs = map (
            partial(get_row_column_pair, base), 
            cell_indices
        )
        self.assertEqual(list(all_pairs), supposed_pairs)

if __name__ == '__main__':
    unittest.main()