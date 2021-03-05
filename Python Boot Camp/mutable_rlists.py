def cons(left, right):
    def data(which, value = None):
        nonlocal left, right
        if which == 0:
            return left
        if which == 1:
            return right
        if which == 2:
            left = value
        else:
            right = value
    return data

def left(pair):
    return pair(0)

def right(pair):
    return pair(1)

def set_left(pair, val):
    pair(2, val)

def set_right(pair, val):
    pair(3, val)

#--------Rlist Methods--------#
empty_rlist = None

def make_rlist(first, rest = empty_rlist):
	"""A recursive list, r, such that first(r) is FIRST and rest(r) is REST, which must be an rlist."""
	return cons(first, rest)

first = left
rest = right
set_first = set_left
set_rest = set_right

def isempty(r):
	"""True iff R is the empty sequence"""
	return r == empty_rlist
