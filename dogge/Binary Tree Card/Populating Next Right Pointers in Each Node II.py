"""
# Definition for a Node.
"""


class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        """
        BFS
        """
        o = root
        if root:
            queue = [root]
            while queue:
                sub_q = []
                while queue:
                    n = queue.pop()
                    if queue:
                        n.next = queue[-1]
                    if n.left:
                        sub_q.insert(0, n.left)
                    if n.right:
                        sub_q.insert(0, n.right)
                queue = sub_q
        return o

    def connect_pointer(self, root: 'Node') -> 'Node':
        """
        pointer way
        """
        cur = root
        while cur:
            child_start = child_point = Node(val=-1, left=None, right=None, next=None)
            while cur:
                if cur.left:
                    child_point.next = cur.left
                    child_point = child_point.next
                if cur.right:
                    child_point.next = cur.right
                    child_point = child_point.next
                cur = cur.next
            cur = child_start.next
        return root
