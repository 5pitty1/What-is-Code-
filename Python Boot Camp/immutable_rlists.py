def cons(left, right):
	return lambda which: left if which else right

def left(pair): return pair(True)
def right(pair): return pair(False)


#--------Rlist Methods--------#
empty_rlist = None
def make_rlist(first, rest = empty_rlist):
	"""A recursive list, r, such that first(r) is FIRST and rest(r) is REST, which must be an rlist."""
	return cons(first, rest)

first = left
rest = right

def isempty(r):
	"""True iff R is the empty sequence"""
	return r == empty_rlist

def print_rlist(r):
	if isempty(r):
		return None
	print(first(r))
	print_rlist(rest(r))
