class DepthLimitedSearch:
    def __init__(self, graph):
        self.graph = graph

    def dls(self, start, goal, limit):
        def recursive_dls(node, depth):
            if depth > limit:  # Exceeded the depth limit
                return "Cutoff"
            if node == goal:  # Found the goal
                return [node]
            if depth == limit:  # Reached depth limit
                return "Cutoff"
            
            cutoff_occurred = False
            for neighbor in self.graph.get(node, []):
                result = recursive_dls(neighbor, depth + 1)
                if result == "Cutoff":
                    cutoff_occurred = True
                elif result is not None:  # Found a solution
                    return [node] + result
            
            return "Cutoff" if cutoff_occurred else None
        
        return recursive_dls(start, 0)

# Get user input to build the graph
def get_user_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes in the graph: "))

    for _ in range(num_nodes):
        node = input("Enter node name: ")
        neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
        graph[node] = neighbors
    
    return graph

if __name__ == "__main__":
    # Get user input
    graph = get_user_graph()
    start_node = input("Enter the start node: ")
    goal_node = input("Enter the goal node: ")
    depth_limit = int(input("Enter the depth limit: "))

    # Perform Depth-Limited Search
    dls = DepthLimitedSearch(graph)
    result = dls.dls(start_node, goal_node, depth_limit)

    # Output the results
    print("\nDepth-Limited Search Result:")
    if result == "Cutoff":
        print("Cutoff occurred. Goal not found within the depth limit.")
    elif result is None:
        print("Goal not found.")
    else:
        print(f"Path to goal: {' -> '.join(result)}")
