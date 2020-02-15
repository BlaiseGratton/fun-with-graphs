#         1  2  3  4  5  6  7  8  9  10
graph = [[0, 0, 1, 0, 0, 0, 0, 0, 0, 0], #  1
         [0, 0, 1, 0, 0, 0, 0, 0, 0, 0], #  2
         [1, 1, 0, 1, 0, 0, 0, 0, 0, 0], #  3
         [0, 0, 1, 0, 1, 0, 1, 0, 0, 0], #  4
         [0, 0, 0, 1, 0, 1, 0, 0, 0, 0], #  5
         [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], #  6
         [0, 0, 0, 1, 0, 0, 0, 1, 0, 0], #  7
         [0, 0, 0, 0, 0, 0, 1, 0, 1, 0], #  8
         [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], #  9
         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]] #  10


def depth_first_search(graph, start_node_index, end_node_index):
    start_node = graph[start_node_index]
    end_node = graph[end_node_index]
    visited = set([start_node_index])

    return search_for_node(graph, start_node, end_node, visited)

def search_for_node(graph, current_node, end_node, visited):
    self_index = graph.index(current_node)
    print('On node {}'.format(self_index + 1))

    if current_node == end_node:
        return True

    found = False

    for index, edge in enumerate(current_node):
        if index == self_index:
            continue
        if edge:
            visited.add(index)
            found = search_for_node(graph, graph[index], end_node, visited)
            if found:
                break
    return found


print(depth_first_search(graph, 3, 0))
