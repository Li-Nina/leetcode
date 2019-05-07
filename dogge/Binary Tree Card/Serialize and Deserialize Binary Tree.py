from ast import literal_eval

# Definition for a binary tree node.
"""
You may serialize the following tree:

    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]"
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        rst = {}

        def ser_node(node: 'TreeNode', index: int):
            rst[index] = node.val
            if node.left:
                ser_node(node.left, index * 2)
            if node.right:
                ser_node(node.right, index * 2 + 1)

        if root:
            ser_node(root, 1)
        return str(rst)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        mapping = literal_eval(data)

        def deser_node(index: int):
            if index in mapping:
                node = TreeNode(mapping[index])
                node.left = deser_node(index * 2)
                node.right = deser_node(index * 2 + 1)
                return node

        return deser_node(1)


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

if __name__ == '__main__':
    x = Codec().deserialize("{}")
    print(x)
