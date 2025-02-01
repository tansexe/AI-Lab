import heapq

# Define the goal state
GOAL_STATE = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

# Heuristic function: Manhattan Distance
def heuristic(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                goal_row, goal_col = divmod(state[i][j], 3)
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance

# Function to find the position of the empty tile (0)
def find_empty_tile(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
    return None

# Function to generate possible moves
def generate_moves(state):
    moves = []
    empty_i, empty_j = find_empty_tile(state)
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_i, new_j = empty_i + di, empty_j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = [row[:] for row in state]
            new_state[empty_i][empty_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[empty_i][empty_j]
            moves.append(new_state)
    return moves

# A* Algorithm
def solve_puzzle(start_state, output_file):
    open_list = []
    heapq.heappush(open_list, (0, 0, start_state, []))  # (f(n), g(n), state, path)
    closed_set = set()

    with open(output_file, "w") as f:
        while open_list:
            f_n, g_n, current_state, path = heapq.heappop(open_list)
            f.write(f"Step {len(path)}:\n")
            f.write("State:\n")
            for row in current_state:
                f.write(f"{row}\n")
            f.write(f"g(n) = {g_n}, h(n) = {heuristic(current_state)}, f(n) = {f_n}\n")
            f.write("------\n")

            if current_state == GOAL_STATE:
                f.write("Goal State Reached!\n")
                return path

            closed_set.add(tuple(map(tuple, current_state)))

            for move in generate_moves(current_state):
                if tuple(map(tuple, move)) not in closed_set:
                    new_g_n = g_n + 1
                    new_f_n = new_g_n + heuristic(move)
                    heapq.heappush(open_list, (new_f_n, new_g_n, move, path + [move]))

    return None

# Start state
START_STATE = [
    [7, 2, 4],
    [5, 0, 6],
    [8, 3, 1]
]

# Output file
OUTPUT_FILE = "output.txt"

# Solve the puzzle and save output to file
solution = solve_puzzle(START_STATE, OUTPUT_FILE)
if solution:
    with open(OUTPUT_FILE, "a") as f:
        f.write("Solution Path:\n")
        for step, state in enumerate(solution):
            f.write(f"Step {step + 1}:\n")
            for row in state:
                f.write(f"{row}\n")
            f.write("------\n")
else:
    with open(OUTPUT_FILE, "a") as f:
        f.write("No solution found.\n")