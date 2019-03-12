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
    inorder = [9,3,15,20,7]     (left)root(right)
    postorder = [9,15,7,20,3]   (left)(right)root
    """

    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> TreeNode:
        if postorder:
            root = postorder[-1]
            root_index = inorder.index(root)

            left_ino = inorder[0:root_index]
            right_ino = inorder[root_index + 1:]

            left_post = postorder[0:len(left_ino)]
            right_post = postorder[len(left_ino):-1]

            o = TreeNode(root)
            if left_post:
                o.left = self.buildTree(left_ino, left_post)
            if right_post:
                o.right = self.buildTree(right_ino, right_post)
            return o
