# Definition for a binary tree node.
"""
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

5->4->11->2 which sum is 22.
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def recursive(node: TreeNode, num):
            if node.left == node.right is None:
                return num + node.val == sum
            else:
                left_bool = recursive(node.left, num + node.val) if node.left else False
                right_bool = recursive(node.right, num + node.val) if node.right else False
                return left_bool or right_bool

        return root is not None and recursive(root, 0)

    def hasPathSum_dfs_iteration(self, root: TreeNode, sum: int) -> bool:
        if root:
            stack = [(root, 0)]
            while stack:
                node, num = stack.pop()
                num += node.val
                if node.left == node.right is None and num == sum:
                    return True
                if node.left:
                    stack.append((node.left, num))
                if node.right:
                    stack.append((node.right, num))
        return False
