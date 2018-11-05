# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# DFS pop() append()
# class Solution(object):
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if root is None:
#             return True
#         stack_left = [root.left]
#         stack_right = [root.right]
#         while len(stack_left) > 0 and len(stack_right) > 0:
#             left = stack_left.pop()
#             right = stack_right.pop()
#             if left is None and right is None:
#                 continue
#             elif left is None or right is None:
#                 return False
#             if left.val != right.val:
#                 return False
#             else:
#                 stack_left.append(left.left)
#                 stack_left.append(left.right)
#                 stack_right.append(right.right)
#                 stack_right.append(right.left)
#         return len(stack_left) == 0 and len(stack_right) == 0
# BFS pop() insert()
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        queuel_left = [root.left]
        queuel_right = [root.right]
        while len(queuel_left) > 0 and len(queuel_right) > 0:
            left = queuel_left.pop()
            right = queuel_right.pop()
            if left is None and right is None:
                continue
            elif left is None or right is None:
                return False
            if left.val != right.val:
                return False
            else:
                queuel_left.insert(0, left.left)
                queuel_left.insert(0, left.right)
                queuel_right.insert(0, right.right)
                queuel_right.insert(0, right.left)
        return len(queuel_left) == 0 and len(queuel_right) == 0
a = TreeNode(2)
b = TreeNode(3)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(5)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f
print(Solution().isSymmetric(a))
