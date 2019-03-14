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
        :param root:
        :return:
        """
        if root:
            pre = None
            queue = [root]
            while queue:
                _q = []
                for n in queue:
                    if pre:
                        pre.next = n
                    if n.left:
                        _q.append(n.left)
                    if n.right:
                        _q.append(n.right)
                    pre = n
                pre = None
                queue = _q
        return root

    def connect_2(self, root: 'Node') -> 'Node':
        """
        BFS
        :param root:
        :return:
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
