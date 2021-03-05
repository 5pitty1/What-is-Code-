
def powerN(base, n):
    """ Return base to the power of n. """
    def powerN2(base, n, total):
        assert n >= 1
        if n == 1:
            return base
        return powerN2(base, n-1, total * base)
    powerN2(base, n, 1)



def triangle(N):
    """ Return the number of blocks in N rows of triangles """
    if N == 0:
        return 0
    return N + triangle(N-1)





def num_path(blocked, x0, y0): "
	""True iff there is a path of squares from (X0, Y0) to some square (x1, 0) such that all squares on 	the path (including first and last) are unoccupied. BLOCKED is a predicate such that BLOCKED(x, 	y) is true iff the grid square	at (x, y) is occupied or off the edge. Each step of a path goes down 	one row and 1 or 0 columns left or right."""
    if blocked(x0, y0):
        return 0
    elif y0 == 0:
        return 1
    else:
        return is_path(blocked, x0-1, y0-1) + is_path(blocked, x0 y0-1) + is_path(blocked, x0+1, y0-1)




def sumN(N):
    """Sum the digits of N"""
    if N < 10:
        return N
    single_digit = N%10
    rest_num = N // 10
    return single_digit + sumN(rest_num)
