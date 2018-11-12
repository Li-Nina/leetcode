# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        queue = []
        if not root:
            return result
        else:
            queue.append(root)
        while queue:
            sub = []
            for i in queue:
                if i.left:
                    sub.append(i.left)
                if i.right:
                    sub.append(i.right)
            result.append([i.val for i in queue])
            queue = sub
        return result
