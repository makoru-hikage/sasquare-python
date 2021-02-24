from .helpers import *

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