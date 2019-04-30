'''
A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return self.val


def is_unival(root):
    if root == None:
        return True

    if root.left != None and root.left.val != root.val:
        return False
    if root.right != None and root.right.val != root.val:
        return False

    if is_unival(root.left) and is_unival(root.right):
        return True
    return False

def count_univals(root):
    if root == None:
        return 0

    total_count = count_univals(root.left) + count_univals(root.right)
    if is_unival(root):
        total_count += 1
    return total_count


if __name__ == '__main__':
    root = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

    print(count_univals(root))
