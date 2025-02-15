class graph:
    def __init__(self,vertex,edges):
        self.adj_mat = []
        self.vertex = vertex
        self.edges = edges
        for i in range(self.vertex):
            self.adj_mat.append([0 for j in range(self.vertex)])

    def undirected_Adj(self):
        for i in range(self.edges):
            A,B = map(int,input("Enter vertex that has edges between them: ").split())
            self.adj_mat[A][B] = 1
            self.adj_mat[B][A] = 1

    def direcected_Adj(self):
        for i in range(self.edges):
            A,B = map(int,input("Enter vertex that has edges between them: ").split())
            self.adj_mat[A][B] = 1

    def undirected_weighted_Adj(self):
        for i in range(self.edges):
            A,B = map(int,input("Enter vertex that has edges between them(DON'T REPEAT): ").split())
            weight = int(input(f"Enter the weight btw ({A},{B}): "))
            self.adj_mat[A][B] = weight
            self.adj_mat[B][A] = weight
    
    def directed_weighted_Adj(self):
        for i in range(self.edges):
            A,B = map(int,input("Enter vertex that has edges between them(DON'T REPEAT): ").split())
            weight = int(input(f"Enter the weight btw ({A},{B}): "))
            self.adj_mat[A][B] = weight
        
    def Display(self):
        print("    ",end ="")
        for k in range(self.vertex):
            print(k,end = " ")
        print()
        for i in range(self.vertex):
            print(i,":",end = " ")
            for j in range(self.vertex):
                print(self.adj_mat[i][j], end = " ")
            print()

ver = int(input("Enter no:of vertices: "))
edge = int(input("Enter no:of edges: "))
obj = graph(ver,edge)
choice = int(input("1.undirected graph\n2.undirected weighted graph\n3.directed graph\n4.directed weigthed graph\n5.display\nEnter your choice: "))
if choice == 1:
    obj.undirected_Adj()
elif choice == 2:
    obj.undirected_weighted_Adj
elif choice == 3:
    obj.direcected_Adj()
elif choice == 4:
    obj.directed_weighted_Adj()
elif choice == 5:
    obj.Display()