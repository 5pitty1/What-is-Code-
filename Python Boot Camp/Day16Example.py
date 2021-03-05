class Backwards:
    def __init__(self, L):
        self._L, self._k = L, len(L) - 1
    def __iter__(self):
        return Backwards(self._L)
    def __next__(self):
        if self._k < 0:
                raise StopIteration
        else:
            self._k -= 1
            return self._L[self._k+1]

x = [3,6,2,8]
