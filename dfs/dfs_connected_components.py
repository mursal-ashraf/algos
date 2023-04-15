
def connected_components(graph):
    def dfs(u, comp_num):
        component[u] = comp_num
        for neighbour in graph[u]:
            if component[neighbour] is None:
                dfs(neighbour, comp_num)

    component = [None for _ in range(len(graph))]
    num_components = 0
    
    # loop over all vertices in case if graph is not connected
    for vertex in range(len(graph)):
        if component[vertex] is None:
            num_components += 1
            dfs(vertex, num_components)
    return num_components


graph = [[2, 3], [4,5,6], [0,3], [2], [5,1], [4,6,1], [1,5]]

print(connected_components(graph))
