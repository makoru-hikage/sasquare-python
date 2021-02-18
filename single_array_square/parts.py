import math

def get_row_index(base, cell_index):
    i = cell_index
    return math.ceil(i/base)

def get_column_index(base, cell_index):
    i = cell_index
    return i - base * int(math.ceil(i/base)) + base

def get_median_base(base):
    return int(math.floor((base + 1) / 2))

def get_opposite_index(length, index):
    return length + 1 - index

def get_intersection_index (row_index, column_index, base):
    r = row_index
    c = column_index
    return c + r*base - base

def get_intersection_sum(base, cell_index):
    r = get_row_index(cell_index)
    c = get_column_index(cell_index)
    return r + c

def get_intersection_diff(base, cell_index):
    r = get_row_index(cell_index)
    c = get_column_index(cell_index)
    return r - c

def count_square_slopes(base):
    return 2*base - 1

def get_descending_index(base, cell_index):
    intersection_diff = get_intersection_diff(base, cell_index)
    return base - intersection_diff

def get_ascending_index(base, cell_index):
    intersection_sum = get_intersection_sum(base, cell_index)
    return intersection_sum - 1

def count_slope_cells(base, slope_index):
    return base - abs(base - slope_index)