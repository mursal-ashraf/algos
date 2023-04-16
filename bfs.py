from collections import deque

"""
Breadth first search traversal of a graph in a adjacency list representation.

Time Complexity: O(V + E) where V and E are the number of vertices and edges respectively

A formal way of describing BFS would be that it visits all vertices at K distance from 
the starting point before visiting any vertices that have a distance of K+1.

It produces a shortest path tree, where every path from the starting point is a shortest
path in the original graph.

Algorithm maintains a queue which contains vertices that need to be visited.
"""


def bfs(graph, start):
    visited = [False for _ in range(len(graph))]
    visited[start] = True
    queue = deque()
    queue.append(start)
    while len(queue) > 0:
        current = queue.popleft()
        for adjacent in graph[current]:
            if not visited[adjacent]:
                visited[adjacent] = True
                queue.append(adjacent)


graph = [[1, 2], [3], [4, 5, 6], [4], [], [], [0]]
bfs(graph, 0)
