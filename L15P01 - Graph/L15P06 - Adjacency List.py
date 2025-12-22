# Create an adjacency list
# Given a no weight direct graph is illustrated in adjacent matrix. 
# Please build adjacent list from given matrix after that using adjacent list to print edge list of graph.

# Input Format
# The first line is number of vertices N
# N next lines contain N number in matrix C building up adjacent matrix.
#   If C(i,j)=0: no edge between vertice i and j
#   If C(i,j)=1: connection edge between vertice i and j
# Vertices are marked from 0 to N - 1. Ensure that C(i,j)=0 with every vertice i

# Output
# The first line is number of edges M
# M next lines contain 2 integers u, v describing for edge (u,v)

# Note: Print edges following the lexicographical order

n = int(input())

adj_matrix = []
for i in range(n):
    new_row = list(map(int, input().split()))
    adj_matrix.append(new_row)
    
adj_list = [[] for _ in range(n)]
edge_count = 0
for u in range(n):
    for v in range(n):
        if adj_matrix[u][v] == 1:
            edge_count += 1
            adj_list[u].append(v)
            
print(edge_count)

for u in range(n):
    for v in adj_list[u]:
        print(u,v)