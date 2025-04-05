from collections import deque

def water_jug_bfs(capacity_a, capacity_b, capacity_c, target):
    queue = deque([((0, 0, 0), [])])
    visited = set()

    while queue:
        (a, b, c), path = queue.popleft()

        if a == target or b == target or c == target:
            return path + [(a, b, c)]

        # All possible operations
        next_states = set()

        # Fill each jug
        next_states.add((capacity_a, b, c))
        next_states.add((a, capacity_b, c))
        next_states.add((a, b, capacity_c))

        # Empty each jug
        next_states.add((0, b, c))
        next_states.add((a, 0, c))
        next_states.add((a, b, 0))

        # Pour between jugs (A<->B, A<->C, B<->C)
        transfers = [
            (0, 1), (1, 0),
            (0, 2), (2, 0),
            (1, 2), (2, 1)
        ]
        current = (a, b, c)
        capacities = [capacity_a, capacity_b, capacity_c]

        for from_jug, to_jug in transfers:
            amounts = list(current)
            pour_amount = min(amounts[from_jug], capacities[to_jug] - amounts[to_jug])
            if pour_amount > 0:
                amounts[from_jug] -= pour_amount
                amounts[to_jug] += pour_amount
                next_states.add(tuple(amounts))

        for next_state in next_states:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(a, b, c)]))

    return None  # No solution found

def get_positive_int_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

def main():
    print("Welcome to the 3-Jug Water Problem Solver!")
    
    capacity_a = get_positive_int_input("Enter the capacity of Jug A: ")
    capacity_b = get_positive_int_input("Enter the capacity of Jug B: ")
    capacity_c = get_positive_int_input("Enter the capacity of Jug C: ")
    target = get_positive_int_input("Enter the target volume: ")

    print(f"\nSolving the Water Jug Problem with:")
    print(f"Jug A capacity: {capacity_a}")
    print(f"Jug B capacity: {capacity_b}")
    print(f"Jug C capacity: {capacity_c}")
    print(f"Target volume: {target}")

    solution = water_jug_bfs(capacity_a, capacity_b, capacity_c, target)

    if solution:
        print("\nSolution found:")
        for i, (a, b, c) in enumerate(solution):
            print(f"Step {i}: Jug A: {a}, Jug B: {b}, Jug C: {c}")
    else:
        print("\nNo solution found for the given inputs.")

    print("\nWould you like to solve another problem?")
    if input("Enter 'y' for yes, any other key to exit: ").lower() == 'y':
        main()
    else:
        print("Thank you for using the 3-Jug Water Problem Solver!")

if __name__ == "__main__":
    main()
