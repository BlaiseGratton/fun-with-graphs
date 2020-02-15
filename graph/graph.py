from .node import Node


class Graph:

    def __init__(self, *node_names):
        self.nodes = set()

        for name in node_names:
            self.add_node(name)

    def add_node(self, name):
        self.nodes.add(Node(name))

    def find_node(self, name):
        for node in self.nodes:
            if node.name == name:
                return node

        raise ValueError('Node {} not found in graph'.format(name))

    def connect_nodes(self, name1, name2):
        node1 = self.find_node(name1)
        node2 = self.find_node(name2)
        node1.connect(node2)

    def __repr__(self):
        return self.nodes.__repr__()



    ############################################
    # Search algorithms                        #
    ############################################


    def depth_first_search(self, start_name, end_name):
        start_node = self.find_node(start_name)
        end_node = self.find_node(end_name)
        visited = set([start_node])

        return self._search_for_node(start_node, end_node, visited)

    def _search_for_node(self, current_node, end_node, visited):
        print('On node {}'.format(current_node.name)) 

        if current_node == end_node:
            return True

        found = False

        for node in current_node.connected_nodes:
            if node not in visited:
                visited.add(node)
                found = self._search_for_node(node, end_node, visited)
                if found:
                    break
        
        return found

    def breadth_first_search(self, start_name, end_name):
        start_node = self.find_node(start_name)
        end_node = self.find_node(end_name)
        to_check = [start_node] 
        visited = set(to_check)

        found = False

        while len(to_check):
            current_node = to_check.pop(0)
            print('On node {}'.format(current_node.name))

            if current_node == end_node:
                found = True
                break
            for node in current_node.connected_nodes:
                if node not in visited:
                    to_check.append(node)
                    visited.add(node)

        return found
