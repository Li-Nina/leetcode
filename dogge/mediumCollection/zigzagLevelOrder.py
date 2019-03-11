# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> 'List[List[int]]':
        rst = []
        if root:
            stack = [root]
            level = 1
            while stack:
                is_even = level % 2 == 0
                sub_rst = []
                stack = self.level_oper(stack, sub_rst, is_even)
                rst.append(sub_rst)
                level += 1
        return rst

    def level_oper(self, stack, sub_rst, is_even):
        _stack = []
        while stack:
            node = stack.pop()
            sub_rst.append(node.val)
            if is_even:  # even level
                if node.right:
                    _stack.append(node.right)
                if node.left:
                    _stack.append(node.left)
            else:  # odd level
                if node.left:
                    _stack.append(node.left)
                if node.right:
                    _stack.append(node.right)
        return _stack
