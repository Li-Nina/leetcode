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
    inorder = [9,3,15,20,7]
    postorder = [9,15,7,20,3]
    """

    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> TreeNode:
        def recursive(inorder_: 'List[int]', postorder_: 'List[int]'):
            if postorder_:
                root = postorder_[-1]
                index = inorder_.index(root)
                left_inorder = inorder_[0:index]
                right_inorder = inorder_[index + 1:]
                left_postorder = postorder_[0:len(left_inorder)]
                right_postorder = postorder_[len(left_inorder):-1]
                root_node = TreeNode(root)
                root_node.left = recursive(left_inorder, left_postorder)
                root_node.right = recursive(right_inorder, right_postorder)
                return root_node

        return recursive(inorder, postorder)


if __name__ == '__main__':
    x = [1, 2, 3, 4, 5]
    print(x[2:-1])
