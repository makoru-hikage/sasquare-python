from functools import partial
from math import floor

from . import parts
from .helpers import compose

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

def reverse_descending_index(base, descending_index):
    return parts.get_opposite_index(parts.count_square_slopes(base), descending_index)

def slope_index_orientation (base, slope_index):
    return floor(slope_index/base)

def descending_slope_orientation(base, descending_index):
    return compose(partial(slope_index_orientation,base), partial(reverse_descending_index,base))(descending_index)

def ascending_slope_orientation (base, ascending_index):
    return slope_index_orientation(base, ascending_index)

def ascending_base_orientation(base, ascending_index):
    return base**ascending_slope_orientation(base,ascending_index)

def descending_base_orientation(base, descending_index):
    return base**descending_slope_orientation(base,descending_index)

def get_desc_nth_cell(b, d, n):
    id = parts.get_slope_intersection_diff(b, d)
    y = descending_base_orientation(b, d)
    return n + b*n - b + y*abs(id)

def get_asc_nth_cell(b, a, n):
    id = parts.get_slope_intersection_diff(b, a)
    y = ascending_base_orientation(b, a)
    l = parts.count_slope_cells(b, a)
    return b*l + b - b*n - l + n - y*id

def select_descending_slope(base, descending_index):
    cell_count = parts.count_slope_cells(base, descending_index)
    return map (partial(get_desc_nth_cell, base, descending_index), get_line_indices(cell_count))

def select_ascending_slope(base, ascending_index):
    cell_count = parts.count_slope_cells(base, ascending_index)
    return map (partial(get_asc_nth_cell, base, ascending_index), get_line_indices(cell_count))