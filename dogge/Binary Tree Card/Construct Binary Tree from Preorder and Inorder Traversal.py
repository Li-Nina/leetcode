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
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    """

    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> TreeNode:
        def recursive(pre_: 'List[int]', in_: 'List[int]'):
            if pre_:
                root = pre_[0]
                index = in_.index(root)
                l_in = in_[0:index]
                r_in = in_[index + 1:]
                l_pre = pre_[1:len(l_in) + 1]
                r_pre = pre_[len(l_in) + 1:]

                o = TreeNode(root)
                o.left = recursive(l_pre, l_in)
                o.right = recursive(r_pre, r_in)
                return o

        return recursive(preorder, inorder)
