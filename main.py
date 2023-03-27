import sys

def read_graph(file_name):
    with open(file_name, 'r') as f:
        n = int(f.readline())
        graph = [[0] * n for _ in range(n)]
        for i in range(n):
            row = f.readline().split()
            for j in range(n):
                graph[i][j] = int(row[j])
        return graph

def prim_mst(graph):
    n = len(graph)
    visited = set()
    start_node = 0
    visited.add(start_node)
    edges = []
    total_weight = 0
    while len(visited) != n:
        min_edge = sys.maxsize
        x = y = 0
        for i in visited:
            for j in range(n):
                if j not in visited and graph[i][j] != 0 and graph[i][j] < min_edge:
                    min_edge = graph[i][j]
                    x = i
                    y = j
        visited.add(y)
        edges.append((x, y, min_edge))
        total_weight += min_edge
    return total_weight, edges

# Приклад виклику функцій
graph = read_graph('graph.txt') # Першим рядком має стояти цифра, яка вказує кількість вершин
mst = prim_mst(graph)
print(mst)
