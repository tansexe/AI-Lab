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


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': [],
        'F': []
    }
    start_node = 'A'
    goal_node = 'E'
    depth_limit = 2

    dls = DepthLimitedSearch(graph)
    result = dls.dls(start_node, goal_node, depth_limit)

    if result == "Cutoff":
        print("Cutoff occurred. Goal not found within the depth limit.")
    elif result is None:
        print("Goal not found.")
    else:
        print(f"Path to goal: {' -> '.join(result)}")
