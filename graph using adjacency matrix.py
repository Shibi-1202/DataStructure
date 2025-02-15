class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0] * vertices for _ in range(vertices)]
    def add_edge(self, vertex1, vertex2):
        self.adj_matrix[vertex1][vertex2] = 1
        self.adj_matrix[vertex2][vertex1] = 1
    def display(self):
        for row in self.adj_matrix:
            print(row)
vertices = int(input("Enter the number of vertices: "))
g = Graph(vertices)
while True:
    print("\n1. Add Edge\n2. Display Graph\n3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        vertex1 = int(input(f"Enter first vertex (0 to {vertices-1}): "))
        vertex2 = int(input(f"Enter second vertex (0 to {vertices-1}): "))
        g.add_edge(vertex1, vertex2)
    elif choice == 2:
        g.display()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")

