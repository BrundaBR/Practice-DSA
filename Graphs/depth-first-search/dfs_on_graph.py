def dfs_on_graph(adj_list):
	visited=set()
	start="A"
	stack=[start]
	while stack!=[]:
		curr=stack.pop()

		#process
		if curr not in visited:
			visited.add(curr)
			print(curr)
		#add unseen children
		for k,chil in adj_list.items():
			if k==curr:
				for i in chil:	
					if i not in visited:
						stack.append(i)

	
adj_list={
	"A":["B","C"],
	"B":["A","D"],
	"C":["A","D","E"],
	"D":["B","C","E"],
	"E":["C","D"]
}
dfs_on_graph(adj_list)