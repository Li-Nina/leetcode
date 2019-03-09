# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        rst = []
        if root:
            index = 0
            level = [root]
            while index < len(level):
                length = len(level)
                sub_rst = []
                for node in level[index:length]:
                    sub_rst.append(node.val)
                    if node.left:
                        level.append(node.left)
                    if node.right:
                        level.append(node.right)
                index = length
                rst.append(sub_rst)
        return rst


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    print(a[1:5])
