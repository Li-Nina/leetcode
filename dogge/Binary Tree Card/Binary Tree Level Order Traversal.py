# Definition for a binary tree node.
"""
    3
   / \
  9  20
    /  \
   15   7

[
  [3],
  [9,20],
  [15,7]
]
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> 'List[List[int]]':
        rst = []
        if root:
            queue = [root]
            while queue:
                sub = []
                for _ in range(len(queue)):
                    node = queue.pop()
                    sub.append(node.val)
                    if node.left:
                        queue.insert(0, node.left)
                    if node.right:
                        queue.insert(0, node.right)
                rst.append(sub)
        return rst
