'''
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
'''


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    def preorder(root):
        if root:
            ordered_list.append(root.val)
            ordered_list.append(",")
            preorder(root.left)
            preorder(root.right)
        else:
            ordered_list.append("None")
            ordered_list.append(",")

    ordered_list = list()
    preorder(root)
    return "".join(ordered_list[0:-1])


# node = Node('root', Node('left', Node('left.left')), Node('right'))
# print(serialize(node))


def deserialize(s):
    def construct():
        val = next(vals)

        if val == "None":
            return None

        node = Node(val)
        node.left = construct()
        node.right = construct()
        return node

    preOrderedList = s.split(',')
    vals = iter(preOrderedList)
    return construct()


# print(deseralize(serialize(node)).left.left.val)

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
