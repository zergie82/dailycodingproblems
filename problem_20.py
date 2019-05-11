'''
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.

For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.

In this example, assume nodes with the same value are the exact same node objects.

Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.
'''


class Node:
    def __init__(self, val=None, n=None):
        self.val = val
        self.next = n

class LinkedList:
    def __init__(self):
        self.head = None

    def list(self):
        vals = []
        current_node = self.head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        print(vals)

def inter(A, B):
    currentA = A.head
    currentB = B.head

    while currentA is not None:
        while currentB is not None:
            if currentA.val == currentB.val:
                return currentA
            currentB = currentB.next
        currentB = B.head
        currentA = currentA.next

    return LinkedList()


if __name__ == '__main__':
    A = LinkedList()
    B = LinkedList()
    A.head = Node(3, Node(7, Node(8, Node(10))))
    B.head = Node(99, Node(1, Node(8, Node(10))))
