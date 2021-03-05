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

    def isLeaf(self):
        return len(self.branches()) == 0

def load_tree():
    head = None
    with open("problem_18.txt") as f:
        head = Tree(int(f.readline()))
        prev_row = [head]
        current_row = []
        for line in f:
            for num in line.split(" "):
                current_row += [Tree(int(num))]
            for i, tree in enumerate(prev_row):
                tree.addBranch(current_row[i])
                tree.addBranch(current_row[i+1])
            prev_row = current_row
            current_row = []
    return head

triangle = load_tree()

def biggest_total(triangle):
    if triangle.isLeaf():
        return triangle.label()
    return triangle.label() + max([biggest_total(branch) for branch in triangle.branches()])

print(biggest_total(triangle))
