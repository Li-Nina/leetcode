# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder_recursion(self, root: TreeNode) -> 'List[List[int]]':
        rst = []

        def level_order(node: TreeNode):
            if node:
                pass

    def levelOrder_iteration(self, root: TreeNode) -> 'List[List[int]]':
        rst = []
        if root:
            queue = [root]
            while queue:
                rst_sub = []
                sub_queue = []
                while queue:
                    node = queue.pop()
                    rst_sub.append(node.val)
                    if node.left:
                        sub_queue.insert(0, node.left)
                    if node.right:
                        sub_queue.insert(0, node.right)
                queue = sub_queue
                rst.append(rst_sub)
        return rst
