from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    
    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def DFSUtil(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True
        print(v, end=" ")

        # Recur for all neighbors
        for neighbor in self.graph[v]:
            if not visited[neighbor]:
                self.DFSUtil(neighbor, visited)
    
    def DFS(self, start_vertex, num_vertices):
        visited = [False] * num_vertices  # Ensure visited size matches total vertices
        self.DFSUtil(start_vertex, visited)

if __name__ == "__main__":
    g = Graph()

    # Input number of vertices and edges
    num_vertices = int(input("Enter the number of vertices: "))
    num_edges = int(input("Enter the number of edges: "))
    
    print("Enter the edges (u v):")
    for _ in range(num_edges):
        u, v = map(int, input().split())
        if u >= num_vertices or v >= num_vertices:
            print(f"Invalid edge: ({u}, {v}) - Nodes must be less than {num_vertices}")
        else:
            g.addEdge(u, v)

    # Input starting vertex
    start_vertex = int(input("Enter the starting vertex for DFS: "))
    if start_vertex >= num_vertices:
        print(f"Invalid starting vertex: {start_vertex} - Must be less than {num_vertices}")
    else:
        print("Following is Depth First Traversal:")
        g.DFS(start_vertex, num_vertices)