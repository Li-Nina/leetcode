# Definition for a binary tree node
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
# class Solution(object):
#     def isSymmetric(self, root):
#         """
#         :type root: TreeNode
#         :rtype: bool
#         """
#         if root is None:
#             return True
#         queuel_left = [root.left]
#         queuel_right = [root.right]
#         while len(queuel_left) > 0 and len(queuel_right) > 0:
#             left = queuel_left.pop()
#             right = queuel_right.pop()
#             if left is None and right is None:
#                 continue
#             elif left is None or right is None:
#                 return False
#             if left.val != right.val:
#                 return False
#             else:
#                 queuel_left.insert(0, left.left)
#                 queuel_left.insert(0, left.right)
#                 queuel_right.insert(0, right.right)
#                 queuel_right.insert(0, right.left)
#         return len(queuel_left) == 0 and len(queuel_right) == 0
#只建立一个List
# class Solution(object):
#     def isSymmetric(self, root):
#         if not root:
#             return True
#         s = [root.left, root.right]
#         while s:
#             n1 = s.pop()
#             n2 = s.pop()
#             if not n1 and not n2:
#                 continue
#             elif not n1 or not n2:
#                 return False
#             elif n1.val != n2.val:
#                 return False
#             else:
#                 s.append(n1.left)
#                 s.append(n2.right)
#                 s.append(n1.right)
#                 s.append(n2.left)
#         return True
class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True
        return self.check(root.left, root.right)
    def check(self, left, right):
        if not left or not right:
            return not left and not right
        elif left.val != right.val:
            return False
        else:
            return self.check(left.left, right.right) and self.check(left.right, right.left)
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
