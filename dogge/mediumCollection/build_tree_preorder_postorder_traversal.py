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
    postorder = [9,15,7,20,3]   (left)(right)root
    """

    def constructFromPrePost(self, pre: 'List[int]', post: 'List[int]') -> TreeNode:
        if post:
            root = post[-1]
            o = TreeNode(root)
            if len(post) > 1:
                right_index = pre.index(post[-2])  # 后序遍历倒数第二个必为根的右节点

                left_pre = pre[1:right_index]
                right_pre = pre[right_index:]

                left_post = post[0:len(left_pre)]
                right_post = post[len(left_pre):-1]

                if left_pre:
                    o.left = self.constructFromPrePost(left_pre, left_post)
                if right_pre:
                    o.right = self.constructFromPrePost(right_pre, right_post)
            return o
