# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        rst = []
        stack = []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                rst.append(root.val)
                root = root.right
        return rst


if __name__ == '__main__':
    s = ['x', 'b']
    m = s.pop()
    print(m)
    print(s)
