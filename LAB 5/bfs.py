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

# Example grid and test
grid = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

start_position = (0, 0)
treasure_position = (3, 3)

# Run Best-First Search
path_to_treasure = best_first_search(grid, start_position, treasure_position)

# Output the results
print("Best-First Search:")
print(f"Path to treasure: {path_to_treasure}")