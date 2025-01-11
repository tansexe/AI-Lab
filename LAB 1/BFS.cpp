#include <iostream>
#include <queue>
#include <vector>
using namespace std;

class Solution
{
public:
    vector<int> BFS(int numberOfVertices, vector<int> adjacencyList[])
    {
        int visited[numberOfVertices] = {0}; // 0 means not visited, 1 means visited.
        visited[0] = 1;                      // mark the first node as visited.

        queue<int> q;
        q.push(0);
        vector<int> result;

        // iteratation till queue is empty.
        while (!q.empty())
        {
            int node = q.front();   // get the front of the queue and store it in a variable called "node".
            q.pop();                // pop the front of the queue.
            result.push_back(node); // push the node into the result vector.

            for (auto it : adjacencyList[node])
            {
                // if the node is not visited, push it into the queue and mark it as visited.
                if (!visited[it])
                {
                    q.push(it);
                    visited[it] = 1;
                }
            }
        };
        return result;
    };
};

void addingAdjacency(vector<int> adj[], int u, int v)
{
    adj[u].push_back(v);
    adj[v].push_back(u);
}

void print(vector<int> &ans)
{
    for (int i = 0; i < ans.size(); i++)
    {
        cout << ans[i] << " ";
    }
}

int main()
{
    // vector<int> adj[6];

    // addingAdjacency(adj, 0, 1);
    // addingAdjacency(adj, 1, 2);
    // addingAdjacency(adj, 1, 3);
    // addingAdjacency(adj, 0, 4);

    // Solution obj;
    // vector<int> ans = obj.BFS(5, adj);
    // print(ans);

    int numberOfVertices, numberOfEdges;

    cout << "Enter the number of vertices: ";
    cin >> numberOfVertices;

    cout << "Enter the number of edges: ";
    cin >> numberOfEdges;

    vector<int> adj[numberOfVertices];
    
    cout << "Enter the edges (u v):" << endl;
    for (int i = 0; i < numberOfEdges; i++)
    {
        int u, v;
        cin >> u >> v;
        addingAdjacency(adj, u, v);
    }

    Solution obj;
    vector<int> ans = obj.BFS(numberOfVertices, adj);

    cout << "BFS Traversal: ";
    print(ans);

    return 0;
}