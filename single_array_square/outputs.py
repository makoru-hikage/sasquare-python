from .helpers import *
from .selections import *
from .symmetry import *

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
        err = "The index must be between 1 and " + str(slopes_count)
        print(err)

def print_ascending_slope(base, ascending_index):
    if slope_index_is_valid(base, ascending_index):
        print_square_to_stdout(
            base,
            select_ascending_slope(base, ascending_index)
        )
    else:
        slopes_count = count_square_slopes(base)
        err = "The index must be between 1 and " + str(slopes_count)
        print(err)

def print_x_cross(base):
    ## Ensure no duplicates by using set
    set_a = set(select_ascending_slope(base, base))
    set_d = set(select_descending_slope(base, base))
    set_d_trimmed = set_d - set_a
    ## Make the result a tuple as usual
    x = tuple(list(set_a) + list(set_d_trimmed))

    print_square_to_stdout(base, x)

def print_all_corners(base):
    print_square_to_stdout(base, select_all_corners(base))

def print_one_corner(base, index):
    result_tuple = ()
    if index == "tr":
        result_tuple = (select_topright_corner(base),)
    elif index == "tl":
        result_tuple = (select_topleft_corner(base),)
    elif index == "br":
        result_tuple = (select_bottomright_corner(base),)
    elif index == "bl":
        result_tuple = (select_bottomleft_corner(base),)
    else:
        print ("Please input only 'tr', 'tl', 'br', 'bl' or none.\n")
        return None

    print_square_to_stdout(base, result_tuple)

def print_center(base):
    print_square_to_stdout(base, select_center(base))

def print_horizontal_opposites(base, cell_index):
    print_square_to_stdout(
        base,
        (
            cell_index,
            horizontal_opposite(base, cell_index)
        )
    )

def print_vertical_opposites(base, cell_index):
    print_square_to_stdout(
        base,
        (
            cell_index,
            vertical_opposite(base, cell_index)
        )
    )

def print_ascending_opposites(base, cell_index):
    print_square_to_stdout(
        base,
        (
            cell_index,
            ascending_opposite(base, cell_index)
        )
    )

def print_descending_opposites(base, cell_index):
    print_square_to_stdout(
        base,
        (
            cell_index,
            descending_opposite(base, cell_index)
        )
    )