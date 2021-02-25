from .helpers import *
from .selections import *

def unselected_asterisk_cell(selected_cells, index):
    if int(index) in selected_cells:
        return index
    return unselected_cell(index)

def print_base_multiple_newline(base, index):
    if int(index) % base == 0:
        return index + '\n'
    elif int(index) == 1:
        return ' ' + index
    return index

def print_square_to_stdout(base, selected_cells):
    cells = map(
        partial(unselected_asterisk_cell, selected_cells),
        map(
            partial(print_base_multiple_newline, base),
            map(
                pad_cell_by_square_size(base),
                range(1, base**2 + 1)
            )
        )
    )

    print(*cells)

def print_row(base, row_index):
    if row_index_is_valid(base, row_index):
        print_square_to_stdout(base, select_row(base, row_index))
    else:
        err = "The index must be between 1 and " + str(base)
        print(err)

def print_column(base, column_index):
    if column_index_is_valid(base, column_index):
        print_square_to_stdout(base, select_column(base, column_index))
    else:
        err = "The index must be between 1 and " + str(base)
        print(err)

def print_descending_slope(base, descending_index):
    if slope_index_is_valid(base, descending_index):
        print_square_to_stdout(
            base,
            select_descending_slope(base, descending_index)
        )
    else:
        slopes_count = count_square_slopes(base)
        err = "The index must be between 1 and " + slopes_count
        print(err)

def print_ascending_slope(base, ascending_index):
    if slope_index_is_valid(base, ascending_index):
        print_square_to_stdout(
            base,
            select_ascending_slope(base, ascending_index)
        )
    else:
        slopes_count = count_square_slopes(base)
        err = "The index must be between 1 and " + slopes_count
        print(err)

def print_all_corners(base):
    print_square_to_stdout(base, select_all_corners(base))

def print_center(base):
    print_square_to_stdout(base, select_center(base))