"""
Depth first search traversal of a graph represented as an adjacency list, recursive.

Time Complexity: O(V + E) where V and E are the number of vertices and edges respectively

Traverses a graph by following a certain path as deep as possible, then backtracks and looks
for unvisited vertices. Each vertex has a flag whether it's visited or not (can be done with
array or hashmap).

Applications of DFS:
- finding connected components of a graph
- two coloring graphs
- cycle finding
- topological ordering (pre req relationships) of directed, acyclic graph
- finding bridges and cut points
"""


def dfs_traverse(graph):
    def dfs(u):
        visited[u] = True
        for neighbour in graph[u]:
            if not visited[neighbour]:
                dfs(neighbour)

    visited = [False for _ in range(len(graph))]

    # loop over all vertices in case if graph is not connected
    for vertex in range(len(graph)):
        if not visited[vertex]:
            dfs(vertex)
