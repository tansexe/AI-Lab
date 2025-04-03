def dfs_recursive(graph, node, visited=None, rec_stack=None):
    if visited is None:
        visited = set()
    if rec_stack is None:
        rec_stack = set()
    
    if node not in visited:
        print(node, end=" ")  # Process the node
        visited.add(node)
        rec_stack.add(node)  # Add to recursion stack

        for neighbor in graph.get(node, []):
            if neighbor not in visited and dfs_recursive(graph, neighbor, visited, rec_stack):
                return True  # Cycle found
            elif neighbor in rec_stack:
                print("\nCycle Found")
                return True  # Cycle found
        
        rec_stack.remove(node)  # Remove after processing

    return False

# Example graph (with cycle: E -> F -> C)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []  # Cycle here (F → C)
}

print("DFS (Recursive):")
if not dfs_recursive(graph, 'A'):
    print("\nNo cycle detected.")
