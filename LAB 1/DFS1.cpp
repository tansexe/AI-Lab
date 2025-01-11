#include <iostream>
#include <vector>
using namespace std;

class Solution
{
public:
    void dfs(int node, vector<int> adj[], int vis[], vector<int> &ls)
    {
        vis[node] = 1;
        ls.push_back(node);
        // Traverse all its neighbors
        for (auto it : adj[node])
        {
            // If the neighbor is not visited
            if (!vis[it])
            {
                dfs(it, adj, vis, ls);
            }
        }
    }

    // Function to return a list containing the DFS traversal of the graph.
    vector<int> dfsOfGraph(int V, vector<int> adj[])
    {
        int vis[V] = {0};
        int start = 0;
        // Create a list to store the DFS traversal
        vector<int> ls;
        // Call dfs for the starting node
        dfs(start, adj, vis, ls);
        return ls;
    }
};

void addEdge(vector<int> adj[], int u, int v)
{
    adj[u].push_back(v);
    adj[v].push_back(u);
}

void print(const vector<int> &ans)
{
    for (int i = 0; i < ans.size(); i++)
    {
        cout << ans[i] << " ";
    }
    cout << endl;
}

int main()
{
    int numberOfVertices, numberOfEdges;

    // Take the number of vertices and edges as input from the user.
    cout << "Enter the number of vertices: ";
    cin >> numberOfVertices;

    cout << "Enter the number of edges: ";
    cin >> numberOfEdges;

    vector<int> adj[numberOfVertices];

    // Input edges from the user.
    cout << "Enter the edges (u v):" << endl;
    for (int i = 0; i < numberOfEdges; i++)
    {
        int u, v;
        cin >> u >> v;
        addEdge(adj, u, v);
    }

    Solution obj;
    vector<int> ans = obj.dfsOfGraph(numberOfVertices, adj);

    cout << "DFS Traversal: ";
    print(ans);

    return 0;
}
