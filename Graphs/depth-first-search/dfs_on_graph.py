def dfs_on_graph(adj_list):
	visited=[]
	for node in adj_list:
		if node not in visited:
			visited.append(node)
			



adj_list={
	"A":["B","C"],
	"B":["A","D"],
	"C":["A","D","E"],
	"D":["B","C","E"],
	"E":["C","D"]
}
dfs_on_graph(adj_list)