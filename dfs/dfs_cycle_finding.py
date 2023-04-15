
def has_cycle(graph):
    def dfs(u, previous):
        visited[u] = True
        for neighbour in graph[u]:
            if visited[neighbour] and neighbour != previous:
                return True
            if neighbour != previous and dfs(neighbour, u):
                return True
        return False

    visited = [False for _ in range(len(graph))]
    
    # loop over all vertices in case if graph is not connected
    for vertex in range(len(graph)):
        if not visited[vertex] and dfs(vertex, None):
            return True
    return False

graph = [[2], [], [3,0], [2]]
print(has_cycle(graph))