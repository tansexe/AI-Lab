from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def BFS(self, s):
        # Create a visited list with size based on the maximum node in the graph
        visited = [False] * (max(self.graph) + 1)
        queue = []  # Initialize a queue

        queue.append(s)  # Enqueue the starting vertex
        visited[s] = True  # Mark the starting vertex as visited

        while queue:  # Loop until the queue is empty
            s = queue.pop(0)  # Dequeue the front of the queue
            print(s, end=" ")  # Print the current node

            # Iterate through all neighbors of the current node
            for i in self.graph[s]:
                if not visited[i]:  # If the neighbor is unvisited
                    queue.append(i)  # Enqueue the neighbor
                    visited[i] = True  # Mark the neighbor as visited

if __name__ == '__main__':
    g = Graph()
    
    # Input number of edges and edges themselves
    num_edges = int(input("Enter the number of edges: "))
    print("Enter the edges (u v):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        g.addEdge(u, v)

    # Input starting vertex
    start_vertex = int(input("Enter the starting vertex for BFS: "))

    print("Following is Breadth First Traversal:")
    g.BFS(start_vertex)
