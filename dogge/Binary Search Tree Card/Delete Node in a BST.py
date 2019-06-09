# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# todo Wrong Answer
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        def finding_node(node: TreeNode, v: int):
            parent = None
            relation = -1
            while node:
                if node.val == v:
                    return parent, node, relation
                elif node.val > v:
                    parent = node
                    node = node.left
                    relation = 0  # left
                else:
                    parent = node
                    node = node.right
                    relation = 1  # right

        def right_least(node: TreeNode):
            parent = node
            right = node.right
            relation = 1
            while right.left:
                parent = right
                right = right.left
                relation = 0
            return parent, right, relation

        _ = finding_node(root, key)
        if not _:
            return root
        p, n, r = _[0], _[1], _[2]
        if n.left and n.right:
            # have two children
            p_, n_, r_ = right_least(n)
            if r_ == 0:
                p_.left = None
            else:
                p_.right = None

            n_.left = n.left
            n_.right = n.right
            if p:
                if r == 0:
                    p.left = n_
                else:
                    p.right = n_
            else:
                root = n_
        elif not (n.left or n.right):
            # have no children
            if p:
                if r == 0:
                    p.left = None
                else:
                    p.right = None
            else:
                root = None
        else:
            # have one child
            if p:
                if r == 0:
                    p.left = n.left if n.left else n.right
                else:
                    p.right = n.left if n.left else n.right
            else:
                root = n.left if n.left else n.right
        return root


if __name__ == '__main__':
    def a():
        pass


    x, y, c = a()
    print(x)
    print(y)
    print(c)
