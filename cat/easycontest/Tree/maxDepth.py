# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    #深度优先
    # def maxDepth(self, root):
    #     """
    #     :type root: TreeNode
    #     :rtype: int
    #     """
    #     if root is None:
    #         return 0
    #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
    #广度优先
    # def maxDepth(self,root):
    #     if root is None:
    #         return 0
    #     depth = 0
    #     list_q = [root]
    #     while len(list_q)!=0:
    #         depth += 1
    #         for i in range(0,len(list_q)):
    #             if list_q[0].left:
    #                 list_q.append(list_q[0].left)
    #             if list_q[0].right:
    #                 list_q.append(list_q[0].right)
    #             del list_q[0]
    #     return depth

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        if root is not None:
            stack.append((1, root))

        depth = 0
        while stack != []:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(depth, current_depth)
                stack.append((current_depth + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth
a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
a.left = b
a.right = c
c.left = d
c.right = e
print(Solution().maxDepth(a))