
class Node:

    def __init__(self, name):
        self.name = name
        self.connected_nodes = set()

    def connect(self, node):
        self.connected_nodes.add(node)
        node.connected_nodes.add(self)

    def disconnect(self, node):
        node.connected_nodes.discard(self)
        self.connected_nodes.discard(node)

    def __repr__(self):
        name = 'Node {}:'.format(self.name)

        connected = (
            '  {} connection(s):'.format(len(self.connected_nodes))
            if self.connected_nodes
            else 'No connections'
        )

        neighbors = '   ' + ', '.join(str(node.name)
                                      for node in self.connected_nodes)

        return '\n' + '\n'.join((name, connected, neighbors))
