# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrderBottom(self, root):
        """
        BFS
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rst = []
        if root:
            queue = [root]
            stack = []
            while queue:
                sub_list = []
                size = len(queue)
                for i in range(size):
                    node = queue.pop(0)
                    sub_list.append(node.val)
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
                stack.append(sub_list)
            while stack:
                rst.append(stack.pop())
        return rst
