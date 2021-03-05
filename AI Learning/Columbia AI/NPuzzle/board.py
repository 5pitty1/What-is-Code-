class Board:

    def __init__(self, layout):
        self.layout = layout
        self.zero_index = self.layout.index(0)

    def move(self, direction):
        copy = None
        if direction == "Up" and self.zero_index // 3 > 0:
            copy = self.layout[::]
            self.swap(copy, self.zero_index, self.zero_index - 3)

        if direction == "Down" and self.zero_index // 3 < 2:
            copy = self.layout[::]
            self.swap(copy, self.zero_index, self.zero_index + 3)

        if direction == "Left" and self.zero_index % 3 > 0:
            copy = self.layout[::]
            self.swap(copy, self.zero_index, self.zero_index - 1)

        if direction == "Right" and self.zero_index % 3 < 2:
            copy = self.layout[::]
            self.swap(copy, self.zero_index, self.zero_index + 1)

        return Board(copy) if copy else None

    @staticmethod
    def swap(board, i, j):
        temp = board[i]
        board[i] = board[j]
        board[j] = temp

    def print_board(self):
        for i, val in enumerate(self.layout):
            if i % 3 == 2:
                print(val)
            else:
                print(val, end=', ')

    def __hash__(self):
        return hash(tuple(self.layout))

    def __eq__(self, other):

        return self.layout == other.layout

    def __repr__(self):
        return str(self.layout)
