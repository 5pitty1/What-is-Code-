from structures import Stack, Queue, PriorityQueue
from state import State
from board import Board


class Solver:
    goalBoard = Board([0, 1, 2, 3, 4, 5, 6, 7, 8])

    def depth_first_search(self, board):

        moves = ['Up', 'Down', 'Left', 'Right'][::-1]
        frontier = Stack()
        explored = set()

        frontier.push(State(board))
        nodes_expanded = 0

        while not frontier.is_empty():
            curr = frontier.pop()
            explored.add(curr)

            if curr.board == self.goalBoard:
                return curr, nodes_expanded

            nodes_expanded += 1

            for move in moves:
                result = curr.board.move(move)
                if result is not None:
                    result_state = State(result, move, curr, curr.depth + 1)
                    if result_state not in explored and result_state not in frontier:
                        State.max_depth = max(State.max_depth, result_state.depth)
                        frontier.push(result_state)

    def breadth_first_search(self, board):

        moves = ['Up', 'Down', 'Left', 'Right']
        frontier = Queue()
        explored = set()

        frontier.add(State(board))
        nodes_expanded = 0

        while not frontier.is_empty():
            curr = frontier.remove()
            explored.add(curr)

            if curr.board == self.goalBoard:
                return curr, nodes_expanded

            nodes_expanded += 1

            for move in moves:
                result = curr.board.move(move)
                if result is not None:
                    result_state = State(result, move, curr, curr.depth + 1)
                    if result_state not in explored and result_state not in frontier:
                        State.max_depth = max(State.max_depth, result_state.depth)
                        frontier.add(result_state)

    def a_star_search(self, board):

        moves = ['Up', 'Down', 'Left', 'Right']
        frontier = PriorityQueue()
        explored = set()

        frontier.add(State(board))
        nodes_expanded = 0

        while not frontier.is_empty():
            curr = frontier.remove()
            explored.add(curr)

            nodes_expanded += 1

            if curr.board == self.goalBoard:
                return curr, nodes_expanded

            for move in moves:
                result = curr.board.move(move)
                if result is not None:
                    result_state = State(result, move, curr, curr.depth + 1)
                    if result_state not in explored and result_state not in frontier:
                        State.max_depth = max(State.max_depth, result_state.depth)
                        frontier.add(result_state)
