from graph import Graph

graph = Graph(1, 2, 3, 4, 5, 6, 7, 8, 9)
graph.connect_nodes(4, 5)
graph.connect_nodes(5, 6)
graph.connect_nodes(4, 3)
graph.connect_nodes(3, 2)
graph.connect_nodes(3, 1)
graph.connect_nodes(4, 7)
graph.connect_nodes(7, 8)
graph.connect_nodes(8, 9)

print('BFS:')
print(graph.breadth_first_search(4, 1))

print('DFS:')
print(graph.depth_first_search(4, 1))
