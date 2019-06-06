# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.node = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while self.stack or self.node:
            if self.node:
                self.stack.append(self.node)
                self.node = self.node.left
            else:
                n = self.stack.pop()
                self.node = n.right
                return n.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return bool(self.stack or self.node)

    def in_order(self, root: TreeNode):
        stack = []
        rst = []
        while stack or root:
            if root:
                stack.append(root)
                root = root.left
            else:
                n = stack.pop()
                rst.append(n.val)
                root = n.right
        return rst

    # Your BSTIterator object will be instantiated and called as such:
    # obj = BSTIterator(root)
    # param_1 = obj.next()
    # param_2 = obj.hasNext()


if __name__ == '__main__':
    a = {4}
    b = {1, 2, 3}
    x = bool(a) or bool(b)
    print(x)
