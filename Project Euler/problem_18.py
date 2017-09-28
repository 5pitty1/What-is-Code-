class Tree:
    def __init__(self, label, branches=None):
        self._label = label
        self._branches = branches if branches else []

    def addBranch(self, branch):
        self._branches += [branch]

    def branches(self):
        return self._branches

    def label(self):
        return self._label

def load_tree():
    head = None
    with open("problem_18.txt") as f:
        head = Tree(int(f.readline()))
        for line in f:
