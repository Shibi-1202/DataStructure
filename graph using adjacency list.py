class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.graph:
            self.graph[vertex1] = []
        if vertex2 not in self.graph:
            self.graph[vertex2] = []
        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    def display(self):
        for vertex in self.graph:
            print(vertex, ":", self.graph[vertex])
g = Graph()
while True:
    print("\n1. Add Edge\n2. Display Graph\n3. Exit")
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        vertex1 = input("Enter first vertex: ")
        vertex2 = input("Enter second vertex: ")
        g.add_edge(vertex1, vertex2)
    elif choice == 2:
        g.display()
    elif choice == 3:
        break
    else:
        print("Invalid choice. Please try again.")

