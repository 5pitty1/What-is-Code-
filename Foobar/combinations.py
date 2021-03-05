# A generator that creates all lexographically ordered
# sets of size 'size' in the modular space 'mod'
class Combination:
    def __init__(self, size, mod):
        self.size = size
        self.mod = mod
        self.combo = [i for i in range(size)]

    def next(self):
        i = self.size - 1
        while i >= 0:
            self.combo[i] = self.combo[i] + 1

            if self.combo[i] <= (self.mod - (self.size - i)) % self.mod:
                break
            i -= 1

        while i < self.size - 1:
            self.combo[i + 1] = self.combo[i] + 1
            i += 1


# This question boils down to a combinatorial problem: Find 'num_buns' subsets of keys
# using the smallest possible set of keys, such that the union of exactly num_required
# subsets is the full set of keys.
#
# Because of this, and the fact that each bunny should result in an equal amount of keys,
# the problem is equivalent to finding {num_buns choose (num_buns - num_required + 1)} subsets.
# This program uses a systematic counting method to find each subset.
#
# The combinatoric equation also ends up becoming the overall runtime of the program.
def solution(num_buns, num_required):
    if num_required > num_buns:
        return []

    bunnies_per_key = num_buns - num_required + 1

    comboGen = Combination(bunnies_per_key, num_buns)

    bunnies = [[] for i in range(num_buns)]
    key = 0

    while comboGen.combo[0] != num_buns - bunnies_per_key:
        for bunny in comboGen.combo:
            bunnies[bunny].append(key)
        comboGen.next()
        key += 1

    for bunny in comboGen.combo:
        bunnies[bunny].append(key)

    return bunnies
