import heapq
from collections import deque

# Represent the graph as an adjacency list
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

def uniform_cost_search(graph, start, goal):
    """
    Implements Uniform Cost Search (UCS) for a weighted graph.
    """
    # Priority queue to store (cost, node, path)
    pq = []
    heapq.heappush(pq, (0, start, [start]))
    visited = set()
    
    while pq:
        cost, current_node, path = heapq.heappop(pq)
        
        if current_node in visited:
            continue
        visited.add(current_node)
        
        # Goal check
        if current_node == goal:
            return cost, path
        
        # Explore neighbors
        for neighbor, weight in graph[current_node].items():
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
    
    return float('inf'), []  # Return if no path is found


def bfs_unweighted(graph, start, goal):
    #Implements BFS for unweighted graphs.
    
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        current_node, path = queue.popleft()
        
        if current_node in visited:
            continue
        visited.add(current_node)
        
        # Goal check
        if current_node == goal:
            return path
        
        # Explore neighbors
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    return []  # Return if no path is found


# Testing
start_node = 'A'
goal_node = 'D'

# Uniform Cost Search
ucs_cost, ucs_path = uniform_cost_search(graph, start_node, goal_node)
print("Uniform Cost Search:")
print(f"Cost: {ucs_cost}, Path: {ucs_path}")

# BFS (assuming the graph is treated as unweighted)
bfs_path = bfs_unweighted(graph, start_node, goal_node)
print("\nBFS (Unweighted):")
print(f"Path: {bfs_path}")