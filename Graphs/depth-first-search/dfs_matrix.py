class GraphAM:
    def __init__(self,Nodes,isDirected=False,isWeighted=False):
        self.adj_matrix=[[0]*(Nodes+1) for x in range(Nodes+2)]
        self.isDirected=isDirected
        self.isWeighted=isWeighted
    
    def add_edge_weighted(self,x,y,z):
        self.adj_matrix[x][y]=z
        if not self.isDirected:
            self.adj_matrix[y][x]=z
    
    def add_edge(self,x,y):
        self.adj_matrix[x][y]=1
        if not self.isDirected:
            self.adj_matrix[y][x]=1

    def delete_edge(self,x,y):
        self.adj_matrix[x][y]=0
        if not self.isDirected:
            self.adj_matrix[y][x]=0
    
    def return_graph(self):
        return self.adj_matrix

nodes=int(input())
edges=int(input())

graph=GraphAM(nodes,True,True)

connection=[]

for _ in range(edges):
    li=list(map(int, input().split()))
    connection.append(li)

for connect in connection:
    graph.add_edge_weighted(connect[0], connect[1],connect[2])

grp=graph.return_graph()

for i in range(1,nodes+1):
    for j in range(1,nodes+1):
        print(grp[i][j],end=' ')
    print()


#Common Input Format 
'''
For directed non weighted
4
5 
1 2 
2 4 
3 1 
3 4 
4 2 

For directed weighted
4
5
1 2 1
2 4 3
3 1 2
3 4 5
4 2 8
'''