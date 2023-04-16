"""
Determines whether a graph contains a cycle using DFS.

Checks if it's searching an already visited vertex, in which case returns
true. But it needs to have an extra constraint, and make sure that it's not
using the vertex we came from as a cycle, ie a -> b and b <- a. This is where
the parameter p comes in.
"""


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


graph = [[2], [], [3, 0], [2]]
print(has_cycle(graph))
