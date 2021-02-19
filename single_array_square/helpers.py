from functools import reduce

def compose (*func):
    def compose_pair(f, g):
        return lambda x : f(g(x))
    return reduce(compose_pair, func, lambda x: x)

def space_leftpad_number (width, number):
    return str(number).rjust(width, ' ')