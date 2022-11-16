import networkx
import matplotlib.pyplot as plt

def check_bipartite_dfs(graph):
    visited = [False] * len(graph)    # set all vertix not visited
    color = [-1] * len(graph)         # set all colors -1
    def dfs(v, c):          # define dfs search for coloring
        visited[v] = True   # visit vertix v
        color[v] = c        # set color everything we want
        for u in graph[v]:  # serch in neighbours for if not visited yet
            if not visited[u]:
                dfs(u, 1 - c)  # set opposite color
    for i in range(len(graph)): # start of searching
        if not visited[i]:
            dfs(i, 0)
    for i in range(len(graph)):  # check of odd round
        for j in graph[i]:
            if color[i] == color[j]:
                return False
    return True

# test examlple graph
#G_symmetric = networkx.Graph()
#graph = {0: [1, 3], 1: [0, 2], 2: [1, 3], 3: [0, 2], 4: []}
#vertix = list(graph.keys())
#for i in range(len(graph)):
#    for j in range(len(graph[i])):
#        G_symmetric.add_edge(vertix[i],graph[i][j])
G = [0] * 5
filename = ['graph1.edgelist','graph2.edgelist','graph3.edgelist','graph4.edgelist','graph5.edgelist']
for i in filename:
    G = networkx.read_edgelist(i, delimiter=" ", create_using=networkx.Graph(), nodetype=int)
    if check_bipartite_dfs(G) == True:
        networkx.draw_networkx(G)
        plt.show()
        print(f'graph {i} is bipartial')
    else:
        networkx.draw_networkx(G)
        plt.show()
        print(f'graph {i}  is not bipartial graph')

