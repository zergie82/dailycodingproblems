'''
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

    def __str__(self):
        return self.val

def serialize(node):
    values = []
    def encode(node):
        if node:
            nonlocal values
            values.append(str(node.val))
            encode(node.left)
            encode(node.right)
        else:
            values.append('#')
    
    encode(node)

    return ' '.join(values)


def deserialize(data):
    vals = iter(data.split(' '))

    def decode(vals):
        val = next(vals)
        if val == '#':
            return None
        node = Node(val)
        node.left = decode(vals)
        node.righ = decode(vals)
        return node

    return decode(vals)