from functools import partial
from math import floor

from single_array_square.parts import *
from single_array_square.helpers import *

def get_line_indices (base):
    return range(1, base + 1)

def get_row_nth_cell (base, row_index, nth_cell):
    return get_intersection_index(base, row_index, nth_cell)

def get_column_nth_cell (base, column_index, nth_cell):
    return get_intersection_index(base, nth_cell, column_index)

def select_row(base, row_index):
    return tuple(map (
        partial(get_row_nth_cell, base, row_index),
        get_line_indices(base)
    ))

def select_column(base, column_index):
    return tuple(map (
        partial(get_column_nth_cell, base, column_index),
        get_line_indices(base)
    ))

def get_even_square_center_q1(base):
    return get_intersection_index(
        base,
        get_center_index(base),
        get_center_index(base)
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
            get_center_index(base),
            get_center_index(base)
        ),)
    return (
        get_even_square_center_q1(base),
        get_even_square_center_q2(base),
        get_even_square_center_q3(base),
        get_even_square_center_q4(base),
    )

def reverse_descending_index(base, descending_index):
    return get_opposite_index(
        count_square_slants(base),
        descending_index
    )

def get_desc_nth_cell(b, d, n):
    """
    Get the nth cell of a descending slant.

    @param int b: the base of the square
    @param int d: the descending index
    @param int n: the nth cell of the descending index
    """
    return get_intersection_index(b,n,n) \
        + b**(2 + floor(-(d)/b))*abs(b-d)

def get_asc_nth_cell(b, a, n):
    """
    Get the nth cell of an ascending slant.

    @param int b: the base of the square
    @param int a: the descending index
    @param int n: the nth cell of the descending index
    """
    return b**2 - b*n + n - (abs(b-a)*(b-1) + b**floor(a/b)*(b-a))

def select_descending_slant(base, descending_index):
    cell_count = count_slant_cells(base, descending_index)
    return tuple(map(
        partial(get_desc_nth_cell,base, descending_index),
        get_line_indices(cell_count)
    ))

def select_ascending_slant(base, ascending_index):
    cell_count = count_slant_cells(base, ascending_index)
    return tuple(map(
        partial(get_asc_nth_cell, base, ascending_index),
        get_line_indices(cell_count)
    ))

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