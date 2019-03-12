# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
        3
       / \
      9  20
        /  \
       15   7
    preorder = [3,9,20,15,7]    root(left)(right)
    inorder = [9,3,15,20,7]     (left)root(right)
    """

    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> TreeNode:
        if preorder:
            root = preorder[0]
            root_index = inorder.index(root)

            left_ino = inorder[0:root_index]
            right_ino = inorder[root_index + 1:]

            left_pre = preorder[1:len(left_ino) + 1]
            right_pre = preorder[len(left_ino) + 1:]

            o = TreeNode(root)
            if left_pre:
                o.left = self.buildTree(left_pre, left_ino)
            if right_pre:
                o.right = self.buildTree(right_pre, right_ino)
            return o


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    mm = a.index(8)
    print(mm)
