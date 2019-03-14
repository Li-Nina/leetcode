# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect_bfs(self, root: 'Node') -> 'Node':
        node = root
        if root:
            pre = None
            queue = [root]
            while queue:
                _q = []
                for i in queue:
                    if pre:
                        pre.next = i
                    if i.left:
                        _q.append(i.left)
                    if i.right:
                        _q.append(i.right)
                    pre = i
                queue = _q
                pre = None
        return node

    def connect(self, root: 'Node') -> 'Node':
        if root and root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            self.connect(root.left)
            self.connect(root.right)
        return root
