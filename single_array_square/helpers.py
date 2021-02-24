from functools import reduce
from functools import partial
from math import log10
import re

def compose (*func):
    def compose_pair(f, g):
        return lambda x : f(g(x))
    return reduce(compose_pair, func, lambda x: x)

def space_leftpad_number (width, number):
    return str(number).rjust(width, ' ')

def sqr_size_pad_width(base):
    return 1 if base*base == 0 else int(log10(base*base)+1)

def pad_cell_by_square_size(base):
    return partial(space_leftpad_number, sqr_size_pad_width(base))

def unselected_cell(number):
    return re.sub(r"\d", ' ', re.sub(r"\d$", u"\u25FB",str(number)))