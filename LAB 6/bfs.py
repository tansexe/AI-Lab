import heapq

def manhattan_distance(start, goal):
    return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

def best_first_search(grid, start, treasure):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
    
    # Priority queue to store (heuristic, (x, y), path)
    pq = []
    heapq.heappush(pq, (manhattan_distance(start, treasure), start, [start]))
    visited = set()
    
    while pq:
        heuristic, (x, y), path = heapq.heappop(pq)
        
        if (x, y) in visited:
            continue
        visited.add((x, y))
        
        # Check if treasure is found
        if (x, y) == treasure:
            return path
        
        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                new_heuristic = manhattan_distance((nx, ny), treasure)
                heapq.heappush(pq, (new_heuristic, (nx, ny), path + [(nx, ny)]))
    
    return []  # Return empty path if no solution is found

# Get user input
rows = int(input("Enter number of rows in the grid: "))
cols = int(input("Enter number of columns in the grid: "))

# Initialize grid
grid = [[0] * cols for _ in range(rows)]

# Get start position
start_x = int(input("Enter start position x-coordinate: "))
start_y = int(input("Enter start position y-coordinate: "))
start_position = (start_x, start_y)

# Get treasure position
treasure_x = int(input("Enter treasure position x-coordinate: "))
treasure_y = int(input("Enter treasure position y-coordinate: "))
treasure_position = (treasure_x, treasure_y)

# Run Best-First Search
path_to_treasure = best_first_search(grid, start_position, treasure_position)

# Output the results
print("\nBest-First Search Result:")
if path_to_treasure:
    print(f"Path to treasure: {path_to_treasure}")
else:
    print("No path to the treasure found.")
