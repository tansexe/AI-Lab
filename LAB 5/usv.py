import heapq
from collections import deque

def uniform_cost_search(graph, start, goal):
    ## Implements Uniform Cost Search (UCS) for a weighted graph.
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
        for neighbor, weight in graph.get(current_node, {}).items():
            if neighbor not in visited:
                heapq.heappush(pq, (cost + weight, neighbor, path + [neighbor]))
    
    return float('inf'), []  # Return if no path is found

def bfs_unweighted(graph, start, goal):
    ## Implements BFS for an unweighted graph.
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
        for neighbor in graph.get(current_node, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
    
    return []  # Return if no path is found

# Get user input to build the graph
graph = {}
num_nodes = int(input("Enter the number of nodes in the graph: "))

for _ in range(num_nodes):
    node = input("Enter node name: ")
    graph[node] = {}
    num_edges = int(input(f"Enter the number of neighbors for {node}: "))
    
    for _ in range(num_edges):
        neighbor, weight = input(f"Enter neighbor and weight for {node} (format: neighbor weight): ").split()
        graph[node][neighbor] = int(weight)

# Get start and goal nodes
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

# Run Uniform Cost Search
ucs_cost, ucs_path = uniform_cost_search(graph, start_node, goal_node)
print("\nUniform Cost Search:")
if ucs_path:
    print(f"Cost: {ucs_cost}, Path: {ucs_path}")
else:
    print("No path found.")

# Run BFS (assuming the graph is unweighted)
bfs_path = bfs_unweighted(graph, start_node, goal_node)
print("\nBFS (Unweighted):")
if bfs_path:
    print(f"Path: {bfs_path}")
else:
    print("No path found.")