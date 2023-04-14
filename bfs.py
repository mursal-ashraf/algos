from collections import deque

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


graph = [[1, 2], [3], [4,5,6], [4], [], [], [0]]
bfs(graph, 0)