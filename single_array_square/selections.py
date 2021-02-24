from functools import partial
from math import floor

from .parts import *
from .helpers import compose

def get_line_indices (base):
    return range(1, base + 1)

def get_row_nth_cell (base, row_index, nth_cell):
    return get_intersection_index(base, row_index, nth_cell)

def get_column_nth_cell (base, column_index, nth_cell):
    return get_intersection_index(base, nth_cell, column_index)

def select_row(base, row_index):
    return map (
        partial(get_row_nth_cell, base, row_index),
        get_line_indices(base)
    )

def select_column(base, column_index):
    return map (
        partial(get_column_nth_cell, base, column_index),
        get_line_indices(base)
    )

def get_even_square_center_q1(base):
    return get_intersection_index(
        base,
        get_median_base(base),
        get_median_base(base)
    )

def get_even_square_center_q2(base):
    return get_even_square_center_q1(base) + 1

def get_even_square_center_q3(base):
    return get_even_square_center_q1(base) + base

def get_even_square_center_q4(base):
    return get_even_square_center_q1(base) + base + 1

def select_center(base):
    if base % 2 != 0:
        return (get_intersection_index(
            base, 
            get_median_base(base),
            get_median_base(base)
        ),)
    return (
        get_even_square_center_q1(base),
        get_even_square_center_q2(base),
        get_even_square_center_q3(base),
        get_even_square_center_q4(base),
    )

def reverse_descending_index(base, descending_index):
    return get_opposite_index(
        count_square_slopes(base),
        descending_index
    )

def slope_index_orientation (base, slope_index):
    return floor(slope_index/base)

def descending_slope_orientation(base, descending_index):
    return compose(
        partial(slope_index_orientation,base),
        partial(reverse_descending_index,base)
    )(descending_index)

def ascending_slope_orientation (base, ascending_index):
    return slope_index_orientation(base, ascending_index)

def ascending_base_orientation(base, ascending_index):
    return base**ascending_slope_orientation(base,ascending_index)

def descending_base_orientation(base, descending_index):
    return base**descending_slope_orientation(base,descending_index)

def get_desc_nth_cell(b, d, n):
    id = get_slope_intersection_diff(b, d)
    y = descending_base_orientation(b, d)
    return n + b*n - b + y*abs(id)

def get_asc_nth_cell(b, a, n):
    id = get_slope_intersection_diff(b, a)
    y = ascending_base_orientation(b, a)
    l = count_slope_cells(b, a)
    return b*l + b - b*n - l + n - y*id

def select_descending_slope(base, descending_index):
    cell_count = count_slope_cells(base, descending_index)
    return map (
        partial(get_desc_nth_cell,base, descending_index),
        get_line_indices(cell_count)
    )

def select_ascending_slope(base, ascending_index):
    cell_count = count_slope_cells(base, ascending_index)
    return map (
        partial(get_asc_nth_cell, base, ascending_index),
        get_line_indices(cell_count)
    )

def select_topright_corner(base):
    return 1

def select_topleft_corner(base):
    return base

def select_bottomright_corner(base):
    return base*base - (base - 1)

def select_bottomleft_corner(base):
    return base*base

def select_all_corners(base):
    return (
        select_topright_corner(base),
        select_topleft_corner(base),
        select_bottomright_corner(base),
        select_bottomleft_corner(base)
    )