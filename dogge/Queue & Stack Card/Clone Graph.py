"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph_DFS(self, node: 'Node') -> 'Node':
        stack = [node]
        mapping = {node: Node(node.val, [])}
        while stack:
            n = stack.pop()
            n_list = mapping[n].neighbors
            for neighbor in n.neighbors:
                # clone node
                if neighbor not in mapping:
                    stack.append(neighbor)
                    mapping[neighbor] = Node(neighbor.val, [])
                # build edges
                n_list.append(mapping[neighbor])
        return mapping[node]

    def cloneGraph_BFS(self, node: 'Node') -> 'Node':
        queue = [node]
        mapping = {node: Node(node.val, [])}
        while queue:
            n = queue.pop(0)
            n_list = mapping[n].neighbors
            for neighbor in n.neighbors:
                # clone node
                if neighbor not in mapping:
                    queue.append(neighbor)
                    mapping[neighbor] = Node(neighbor.val, [])
                # build edges
                n_list.append(mapping[neighbor])
        return mapping[node]
