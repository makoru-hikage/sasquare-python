from math import floor
from math import ceil

def get_row_index(base, cell_index):
    return ceil(cell_index/base)

def get_column_index(base, cell_index):
    return cell_index - base * int(math.ceil(cell_index/base)) + base

def get_median_base(base):
    return int(floor((base + 1) / 2))

def get_opposite_index(length, index):
    return length + 1 - index

def get_intersection_index (base, row_index, column_index):
    return column_index + row_index*base - base

def get_intersection_sum(base, cell_index):
    return get_row_index(cell_index) + get_column_index(cell_index)

def get_intersection_diff(base, cell_index):
    return get_row_index(cell_index) - get_column_index(cell_index)

def get_slope_intersection_diff (base, descending_index):
    return base - descending_index

def count_square_slopes(base):
    return 2*base - 1

def get_descending_index(base, cell_index):
    return base - get_intersection_diff(base, cell_index)

def get_ascending_index(base, cell_index):
    return get_intersection_sum(base, cell_index) - 1

def count_slope_cells(base, slope_index):
    return base - abs(base - slope_index)