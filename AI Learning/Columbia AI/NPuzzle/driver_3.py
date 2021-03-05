import sys
from board import Board
from solver import Solver
from state import State
from time import time
from resource import getrusage, RUSAGE_SELF


def create_output(state, nodes_expanded, time_taken):
    cost = 0
    path = []
    while state.last_state:
        cost += 1
        path = [state.last_move] + path
        state = state.last_state

    with open("output.txt", "w") as file:
        file.write("path_to_goal: " + str(path) + "\n")
        file.write("cost_of_path: " + str(cost) + "\n")
        file.write("nodes_expanded: " + str(nodes_expanded) + "\n")
        file.write("search_depth: " + str(cost) + "\n")
        file.write("max_search_depth: " + str(State.max_depth) + "\n")
        file.write("running_time: " + str(time_taken) + "\n")
        file.write("max_ram_usage: " + str(getrusage(RUSAGE_SELF).ru_maxrss))


def main():
    method = sys.argv[1]

    given_layout = [int(i) for i in sys.argv[2].split(",")]
    sorted_layout = given_layout[::]
    sorted_layout.sort()

    if sorted_layout != [0, 1, 2, 3, 4, 5, 6, 7, 8]:
        print("Bad board input")
        return

    initial_board = Board(given_layout)
    solver = Solver()

    final_state = None
    nodes_expanded = 0
    start = time()

    if method == "dfs":
        final_state, nodes_expanded = solver.depth_first_search(initial_board)
    elif method == "bfs":
        final_state, nodes_expanded = solver.breadth_first_search(initial_board)
    elif method == "ast":
        final_state, nodes_expanded = solver.a_star_search(initial_board)
    else:
        print("Please choose a proper method")

    end = time()

    time_taken = end - start

    create_output(final_state, nodes_expanded, time_taken)


if __name__ == '__main__':
    main()
