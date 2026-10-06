import heapq

# Goal State
GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)


# --------------------------------------------------
# Manhattan Distance
# --------------------------------------------------
def manhattan(state):
    distance = 0

    for i in range(9):
        tile = state[i]

        if tile == 0:
            continue

        # Current position
        row = i // 3
        col = i % 3

        # Goal position of tile
        goal_pos = tile - 1
        goal_row = goal_pos // 3
        goal_col = goal_pos % 3

        distance += abs(row - goal_row)
        distance += abs(col - goal_col)

    return distance


# --------------------------------------------------
# Display the puzzle
# --------------------------------------------------
def display(state):
    for i in range(0, 9, 3):
        print(" ".join("_" if x == 0 else str(x)
                       for x in state[i:i + 3]))
    print()


# --------------------------------------------------
# Generate possible moves
# --------------------------------------------------
def get_moves(state):

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    moves = []

    # Order chosen to give simple output
    directions = [
        ("UP", -1, 0),
        ("DOWN", 1, 0),
        ("LEFT", 0, -1),
        ("RIGHT", 0, 1)
    ]

    for name, dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            # Swap blank with tile
            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            moves.append((tuple(new_state), name))

    return moves


# --------------------------------------------------
# A* Search
# --------------------------------------------------
def a_star(start):

    # Priority queue:
    # f, g, state, path
    queue = []

    g = 0
    h = manhattan(start)
    f = g + h

    heapq.heappush(queue, (f, g, start, []))

    visited = set()

    while queue:

        f, g, current, path = heapq.heappop(queue)

        if current in visited:
            continue

        visited.add(current)

        # Goal reached
        if current == GOAL:
            return path

        # Generate next states
        for next_state, move in get_moves(current):

            if next_state not in visited:

                new_g = g + 1
                new_h = manhattan(next_state)
                new_f = new_g + new_h

                new_path = path + [(move, next_state)]

                heapq.heappush(
                    queue,
                    (new_f, new_g, next_state, new_path)
                )

    return None


# --------------------------------------------------
# Run Test Case
# --------------------------------------------------
def run_test_case(number, start):

    print("Test Case", number)
    print()

    print("Input:")
    display(start)

    solution = a_star(start)

    print("Output:")
    print()

    if solution:

        for i, (move, state) in enumerate(solution):

            if len(solution) == 1:
                print("Move:", move)
            else:
                print("Move", i + 1, ":", move)

            print()
            display(state)

        print("Goal State Reached")
        print("Solution Cost =", len(solution))

    else:
        print("No solution found.")

    print()
    print("-" * 50)
    print()


# ==================================================
# MAIN PROGRAM
# ==================================================

# Test Case 1
# One move
test1 = (
    1, 2, 3,
    4, 5, 6,
    7, 0, 8
)


# Test Case 2
# Two moves
test2 = (
    1, 2, 3,
    4, 0, 6,
    7, 5, 8
)


# Test Case 3
# Four moves
test3 = (
    1, 2, 3,
    5, 0, 6,
    4, 7, 8
)


run_test_case(1, test1)
run_test_case(2, test2)
run_test_case(3, test3)
