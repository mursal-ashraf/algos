
def dfs_traverse(graph):
    """
    :Input:
        :graph: a graph represented as an adjaceny list
    :Complexity:
        O(V + E) - where V is the number of vertices and E
        is the number of edges
    """
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