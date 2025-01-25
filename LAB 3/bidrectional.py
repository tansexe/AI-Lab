import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

def bidirectional_bfs(graph, start, target):
    if start == target:
        return [start]

    # Initialize two frontiers
    frontier_start = deque([start])
    frontier_target = deque([target])
    visited_start = {start: None}
    visited_target = {target: None}

    while frontier_start and frontier_target:
        # Expand from the start side
        if frontier_start:
            current_start = frontier_start.popleft()
            for neighbor in graph.neighbors(current_start):
                if neighbor not in visited_start:
                    visited_start[neighbor] = current_start
                    frontier_start.append(neighbor)
                    if neighbor in visited_target:
                        return reconstruct_path(visited_start, visited_target, neighbor)

        # Expand from the target side
        if frontier_target:
            current_target = frontier_target.popleft()
            for neighbor in graph.neighbors(current_target):
                if neighbor not in visited_target:
                    visited_target[neighbor] = current_target
                    frontier_target.append(neighbor)
                    if neighbor in visited_start:
                        return reconstruct_path(visited_start, visited_target, neighbor)

    return None

def reconstruct_path(visited_start, visited_target, meeting_node):
    path_start = []
    node = meeting_node
    while node is not None:
        path_start.append(node)
        node = visited_start[node]
    path_start.reverse()

    path_target = []
    node = visited_target[meeting_node]
    while node is not None:
        path_target.append(node)
        node = visited_target[node]

    return path_start + path_target

def bfs(graph, start, target):
    queue = deque([start])
    visited = {start: None}

    while queue:
        current = queue.popleft()
        if current == target:
            path = []
            while current is not None:
                path.append(current)
                current = visited[current]
            return path[::-1]
        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)

    return None

def visualize_graph(graph, path=None):
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=10)
    if path:
        edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
        nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color="red", width=2)
    plt.show()

# Create a city graph
city_map = nx.Graph()
edges = [
    (1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (4, 6),
    (5, 6), (5, 7), (6, 8), (7, 8), (7, 9), (8, 10)
]
city_map.add_edges_from(edges)

# Visualize the city map
print("City Map:")
visualize_graph(city_map)

# User input for start and target
start = int(input("Enter the start intersection: "))
target = int(input("Enter the target intersection: "))

# Run Bi-directional BFS
path_bi = bidirectional_bfs(city_map, start, target)
print(f"Bi-directional BFS Path: {path_bi}")

# Run Standard BFS
path_std = bfs(city_map, start, target)
print(f"Standard BFS Path: {path_std}")

# Visualize the path found by Bi-directional BFS
print("Path Visualized (Bi-directional BFS):")
visualize_graph(city_map, path=path_bi)