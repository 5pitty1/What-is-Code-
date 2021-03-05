class State:

    max_depth = 0

    def __init__(self, board, last_move="", last_state=None, depth=0):
        self.board = board
        self.last_move = last_move
        self.last_state = last_state
        self.depth = depth
        self.heuristic = self.getHeuristic()
        self.total_cost = self.depth + self.heuristic

    def getHeuristic(self):
        heuristic = 0
        for i, val in enumerate(self.board.layout):
            xdist = abs(i % 3 - val % 3)
            ydist = abs(i // 3 - val // 3)
            heuristic += xdist + ydist
        return heuristic

    def __hash__(self):
        return hash(self.board)

    def __eq__(self, other):
        return self.board == other.board

    def __lt__(self, other):
        return self.total_cost < other.total_cost

    def __repr__(self):
        return str(self.board) + " : " + self.last_move


if __name__ == '__main__':
    from board import Board
    board = Board([1,2,5,3,4,0,6,7,8])
    state = State(board)
    print(state.heuristic)
