from collections import deque

def water_jug_bfs(capacity_a, capacity_b, target):
    queue = deque([((0, 0), [])])
    visited = set()

    while queue:
        (a, b), path = queue.popleft()

        if a == target or b == target:
            return path + [(a, b)]

        next_states = [
            (capacity_a, b),  # Fill jug A
            (a, capacity_b),  # Fill jug B
            (0, b),           # Empty jug A
            (a, 0),           # Empty jug B
            (min(a + b, capacity_a), max(0, a + b - capacity_a)),  # Pour B to A
            (max(0, a + b - capacity_b), min(a + b, capacity_b))   # Pour A to B
        ]

        for next_state in next_states:
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [(a, b)]))

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
    print("Welcome to the Water Jug Problem Solver!")
    
    capacity_a = get_positive_int_input("Enter the capacity of jug A: ")
    capacity_b = get_positive_int_input("Enter the capacity of jug B: ")
    target = get_positive_int_input("Enter the target volume: ")

    print(f"\nSolving the Water Jug Problem with:")
    print(f"Jug A capacity: {capacity_a}")
    print(f"Jug B capacity: {capacity_b}")
    print(f"Target volume: {target}")

    solution = water_jug_bfs(capacity_a, capacity_b, target)

    if solution:
        print("\nSolution found:")
        for i, (a, b) in enumerate(solution):
            print(f"Step {i}: Jug A: {a}, Jug B: {b}")
    else:
        print("\nNo solution found for the given inputs.")

    print("\nWould you like to solve another problem?")
    if input("Enter 'y' for yes, any other key to exit: ").lower() == 'y':
        main()
    else:
        print("Thank you for using the Water Jug Problem Solver!")

if __name__ == "__main__":
    main()
