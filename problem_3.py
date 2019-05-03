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
    if node:
        values.append(str(node.val))
        values.append(serialize(node.left))
        values.append(serialize(node.right))
    else:
        values.append('#')

    return ' '.join(values)

def serialize_generator(node):
    if node:
        yield node.val
        for node_val in serialize_generator(node.left):
            yield node_val
        for node_val in serialize_generator(node.right):
            yield node_val
    else:
        yield '#'

def deserialize(data):
    #vals = iter(data.split(' '))
    vals = data

    def decode(vals):
        val = next(vals)
        if val == '#':
            return None
        node = Node(val)
        node.left = decode(vals)
        node.right = decode(vals)
        return node

    return decode(vals)

if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
