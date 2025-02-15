#Dijkstra's algorithm implementation
class Graph:
    def _init_(self):
        self.edges = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.edges:
            self.edges[from_node] = []
        if to_node not in self.edges:
            self.edges[to_node] = []
        self.edges[from_node].append((to_node, weight))
        self.edges[to_node].append((from_node, weight))

    def dijkstra(self, start):
        INF = 99999
        distances = {}
        for node in self.edges:
            distances[node] = INF
        distances[start] = 0
        visited = set()

        while len(visited) < len(self.edges):
            min_node = None
            for node in distances:
                if node not in visited:
                    if min_node is None or distances[node] < distances[min_node]:
                        min_node = node
            if min_node is None or distances[min_node] == INF:
                break
            for neighbor, weight in self.edges[min_node]:
                print(neighbor,weight)
                if neighbor not in visited:
                    new_distance = distances[min_node] + weight
                    if new_distance < distances[neighbor]:
                        distances[neighbor] = new_distance
            visited.add(min_node)
        return distances
graph = Graph()
num_edges = int(input("Enter the number of edges in the graph: "))
for _ in range(num_edges):
    from_node = input("Enter the starting node of the edge: ")
    to_node = input("Enter the ending node of the edge: ")
    weight = int(input(f"Enter the weight of the edge from {from_node} to {to_node}: "))
    graph.add_edge(from_node, to_node, weight)
print(graph.edges)
start_node = input("Enter the starting node for Dijkstra's algorithm: ")
if start_node in graph.edges:
    distances = graph.dijkstra(start_node)
    print("\nShortest distances from the starting node:")
    for node, distance in distances.items():
        print(f"Distance from {start_node} to {node}: {distance}")
else:
    print("Starting node not found in the graph.")
