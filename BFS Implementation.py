#BFS Implementation
def bfs(matrix, start):
    n = len(matrix) 
    visited = [False] * n
    queue = [start]
    visited[start] = True
    result = []

    while queue:
        node = queue.pop(0)
        result.append(node)
        for i in range(n):
            if matrix[node][i] == 1 and not visited[i]: 
                queue.append(i)
                visited[i] = True

    return result

n = int(input("Enter the number of nodes: "))
matrix = []
for i in range(n):
    row=[0]*n
    matrix.append(row)
for i in range(n):
    src=int(input("Enter the src value"))
    dist=int(input("Enter the dist value"))
    matrix[src][dist]=1
    matrix[dist][src]=1
start = int(input("Enter the starting node (0 to n-1): "))
print("BFS traversal:", bfs(matrix, start))
