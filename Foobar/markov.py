from fractions import Fraction, gcd


# Transposes given matrix
def transposeMatrix(m):
    return [list(i) for i in zip(*m)]


# Recursively compute the determinant of a matrix
def getMatrixDeternminant(m):
    if len(m) == 1:
        return m[0][0]

    determinant = 0
    for c in range(len(m)):
        minor = [row[:c] + row[c + 1 :] for row in m[1:]]
        if c % 2 == 0:
            determinant += m[0][c] * getMatrixDeternminant(minor)
        else:
            determinant -= m[0][c] * getMatrixDeternminant(minor)
    return determinant


# Compute the inverse of a matrix
def getMatrixInverse(m):
    determinant = getMatrixDeternminant(m)

    if len(m) == 1:
        return [[m[0][0] / determinant]]

    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = [row[:c] + row[c + 1 :] for row in (m[:r] + m[r + 1 :])]
            if (r + c) % 2 == 0:
                cofactorRow.append(getMatrixDeternminant(minor))
            else:
                cofactorRow.append(-1 * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = transposeMatrix(cofactors)

    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / determinant
    return cofactors


# Rearrange the elements of arr using the ordering specified in index
def reorder(arr, index, n):
    temp = [arr[index[i]] for i in range(n)]

    for i in range(0, n):
        arr[i] = temp[i]


# Converts m into a standard form markov matrix, returning the number of
# absorbing nodes and the new index ordering
def convertToMarkov(m, size):
    absorbing = []
    non_absorbing = []

    for i in range(size):
        denominator = sum(m[i])
        if denominator == 0:
            m[i][i] = 1
            absorbing.append(i)
        else:
            for j in range(size):
                m[i][j] = Fraction(m[i][j], denominator)
            non_absorbing.append(i)

    newIndex = absorbing + non_absorbing

    for i in range(size):
        reorder(m[i], newIndex, size)

    reorder(m, newIndex, size)

    return len(absorbing), newIndex


# Gets the fundamental matrix from the standard form markov matrix
def getFundamental(m, numAbsorbing):
    Q = [row[numAbsorbing:] for row in m[numAbsorbing:]]
    size = len(Q)

    for i in range(size):
        for j in range(size):
            if i == j:
                Q[i][j] = 1 - Q[i][j]
            else:
                Q[i][j] = -Q[i][j]

    return getMatrixInverse(Q)


# Multiplies two matrices together, assuming it is a valid pair
def matrixMultiply(m, n):
    mSize = len(m)
    nSize = len(n[0])
    iterSize = len(n)

    result = [[0 for j in range(nSize)] for i in range(mSize)]

    for i in range(mSize):
        for j in range(nSize):
            total = 0
            for k in range(iterSize):
                total += m[i][k] * n[k][j]
            result[i][j] = total

    return result


# Calculates the stable markov matrix from the individual components of
# the standard matrix
def buildStable(m, numAbsorbing, FR):
    mSize = len(m)

    result = [[0 for j in range(mSize)] for i in range(mSize)]

    for i in range(numAbsorbing):
        result[i][i] = 1

    for i, row in enumerate(FR):
        for j, val in enumerate(row):
            result[i + numAbsorbing][j] = val

    return result


# Calculates the least common multiple of a and b
def lcm(a, b):
    return abs(a * b) // gcd(a, b)


# This question can be solved efficiently if we consider it as
# an absorbing markov chain. This allows us to use a standardized
# approach to finding the final distribution given an initial distribution
# This allows us to calculate the distributions in constant time and constant
# space
def solution(m):
    if len(m) == 1:
        return [1, 1]

    # First we need to convert our matrix into standard markov form
    numAbsorbing, newIndex = convertToMarkov(m, len(m))

    # Standard Markov form consists of 4 quadrants: I,0, R, Q
    # Using these quadrants, we can find the fundamental matrix
    R = [row[:numAbsorbing] for row in m[numAbsorbing:]]
    fundamental = getFundamental(m, numAbsorbing)

    # And finally, given the fundamnetal matrix and the four quadrandts,
    # we can compute the stable distribution markov matrix
    FR = matrixMultiply(fundamental, R)
    stableMatrix = buildStable(m, numAbsorbing, FR)

    # So all we have to do is matrix multiply our initial distribution of
    # only s0 being filled with our stable matrix to get the final distribution
    initialDistribution = [[1 if i == 0 else 0 for i in newIndex]]
    finalDistribution = matrixMultiply(initialDistribution, stableMatrix)[0]

    # Lastly we convert all probabilities to have the same denominator
    lcmVal = finalDistribution[0].denominator
    for i in range(numAbsorbing):
        lcmVal = lcm(lcmVal, finalDistribution[i].denominator)

    # And we build the desired format for the probability distribution of the
    # absorbing states
    result = []
    for i in range(numAbsorbing):
        multiple = lcmVal // finalDistribution[i].denominator
        result.append(finalDistribution[i].numerator * multiple)
    result.append(lcmVal)

    return result
