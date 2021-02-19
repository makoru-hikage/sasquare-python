from functools import partial
from math import floor

from . import parts
from . import helpers

def get_line_indices (base):
    return range(1, base + 1)

def get_row_nth_cell (base, row_index, nth_cell):
    return parts.get_intersection_index(base, row_index, nth_cell)

def get_column_nth_cell (base, column_index, nth_cell):
    return parts.get_intersection_index(base, nth_cell, column_index)

def select_row(base, row_index):
    return map (partial(get_row_nth_cell, base, row_index), get_line_indices(base))

def select_column(base, column_index):
    return map (partial(get_column_nth_cell, base, column_index), get_line_indices(base))

def select_center(base):
    if base % 2 != 0:
        return (parts.get_intersection_index(
            base, 
            parts.get_median_base(base),
            parts.get_median_base(base)
        ),)
    else:
        q1 = parts.get_intersection_index(base, parts.get_median_base(base), parts.get_median_base(base))
        q2 = q1 + 1
        q3 = q1 + base
        q4 = q1 + base + 1
        return (q1, q2, q3, q4)
