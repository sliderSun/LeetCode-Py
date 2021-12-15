def bfs(graph, start):
	visited = set(start)
	queue = []
	queue.append(start)
	while queue:
		node_u = q.pop(0)
		print(node_u)
		for node_v in graph[node_u]:
			if node_v not in visited:
				visited.add(node_v)
				q.put(node_v)
				

graph = {
	"A": ["B", "C"],
	"B": ["A", "C", "D"],
	"C": ["A", "B", "D", "E"],
	"D": ["B", "C", "E", "F"],
	"E": ["C", "D"],
	"F": ["D"]
}

# 基于队列实现的广度优先搜索
bfs(graph, "A")