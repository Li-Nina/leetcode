"""
To convert a recursion approach to an iteration one, we could perform the following two steps:
1.We use a stack or queue data structure within the function, to replace the role of the system call stack.
At each occurrence of recursion, we simply push the parameters as a new element into the data structure that we created,
instead of invoking a recursion.

2.In addition, we create a loop over the data structure that we created before.
The chain invocation of recursion would then be replaced with the iteration within the loop.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSameTree_recursion(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None or q is None:
            return p == q
        if p.val != q.val:
            return False
        return self.isSameTree_recursion(p.left, q.left) and self.isSameTree_recursion(p.right, q.right)

    def isSameTree_iteration(self, p: TreeNode, q: TreeNode) -> bool:
        def check(t1: TreeNode, t2: TreeNode):
            return t1 == t2 if t1 is None or t2 is None else t1.val == t2.val

        stack = [p, q]
        while stack:
            s1 = stack.pop()
            s2 = stack.pop()
            if not check(s1, s2):
                return False
            if s1:
                stack.append(s1.left)
                stack.append(s2.left)
                stack.append(s1.right)
                stack.append(s2.right)
        return True
