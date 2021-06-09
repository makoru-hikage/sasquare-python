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

    def test_center_of_an_odd_square (self):
        base = 5
        ## a tuple of a lone element is still a tuple
        supposed_cell_index = (13,)

        self.assertEqual(select_center(base), supposed_cell_index)

    def test_center_of_an_even_square (self):
        base = 6
        supposed_cell_indices = (15,16,21,22)

        self.assertEqual(select_center(base), supposed_cell_indices)

    def test_corners_of_b5(self):
        base = 5
        supposed_cell_indices = (1,5,21,25)

        self.assertEqual(
            select_all_corners(base),
            supposed_cell_indices
        )

    def test_n_of_slant_foreach_kind_in_b5(self):
        base = 5
        n_of_all_slants = count_square_slants(base)
        supposed_count = 9

        self.assertEqual(n_of_all_slants, supposed_count)

    def test_descending_slants_of_b5(self):
        base = 5

        slant1 = (21,)
        slant2 = (16,22)
        slant3 = (11,17,23)
        slant4 = (6,12,18,24)
        slant5 = (1,7,13,19,25)
        slant6 = (2,8,14,20)
        slant7 = (3,9,15)
        slant8 = (4,10)
        slant9 = (5,)

        supposed_slants = [
            slant1,
            slant2,
            slant3,
            slant4,
            slant5,
            slant6,
            slant7,
            slant8,
            slant9,
        ]

        n_of_all_slants = count_square_slants(base)

        all_slants = map (
            partial(select_descending_slant, base),
            range (1, n_of_all_slants + 1)
        )

        self.assertEqual(list(all_slants), supposed_slants)

    def test_ascending_slants_of_b5(self):
        base = 5

        slant1 = (1,)
        slant2 = (6,2)
        slant3 = (11,7,3)
        slant4 = (16,12,8,4)
        slant5 = (21,17,13,9,5)
        slant6 = (22,18,14,10)
        slant7 = (23,19,15)
        slant8 = (24,20)
        slant9 = (25,)

        supposed_slants = [
            slant1,
            slant2,
            slant3,
            slant4,
            slant5,
            slant6,
            slant7,
            slant8,
            slant9,
        ]

        n_of_all_slants = count_square_slants(base)

        all_slants = map (
            partial(select_ascending_slant, base),
            range (1, n_of_all_slants + 1)
        )

        self.assertEqual(list(all_slants), supposed_slants)






if __name__ == '__main__':
    unittest.main()