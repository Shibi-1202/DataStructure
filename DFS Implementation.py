#DFS Implementation
class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacency_matrix = []
        for i in range(num_vertices):
            row = [0] * num_vertices
            self.adjacency_matrix.append(row)
        self.visited = []
        for i in range(num_vertices):
            self.visited.append(False)
    def add_edge(self, src, dest):
        self.adjacency_matrix[src][dest] = 1
        self.adjacency_matrix[dest][src] = 1
    def dfs(self, vertex):
        if self.visited[vertex]:
            return
        self.visited[vertex] = True
        print(vertex, end=' ')
        for i in range(self.num_vertices):
            if self.adjacency_matrix[vertex][i] == 1 and not self.visited[i]:
                self.dfs(i)
n=int(input("Enter the number of nodes"))
g = Graph(n)
for i in range(n):
    src=int(input("Enter the src value"))
    dist=int(input("Enter the dist value"))
    g.add_edge(src,dist)
start_node=int(input("Enter the strting node"))
g.dfs(start_node)
