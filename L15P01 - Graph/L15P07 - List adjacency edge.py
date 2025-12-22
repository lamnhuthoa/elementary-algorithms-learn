# List adjacency edge
class Edge:
    def __init__(self, u, v, w):
        self.u = u
        self.v = v
        self.w = w
        
def sort_edges(edges):
    for i in range(1, len(edges)):
        cur = edges[i]
        j = i
        while j > 0 and edges[j - 1].w > cur.w:
            edges[j] = edges[j - 1]
            j -= 1
        edges[j] = cur
        
m, k = map(int, input().split())

edge_list = []
for i in range(m):
    u, v, w = map(int, input().split())
    edge_list.append(Edge(u, v, w))

sort_edges(edge_list)

for i in range(k - 1, -1, -1):
    print(edge_list[i].u, edge_list[i].v)