'''
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.
'''
import ctypes

class Node:
    def __init__(self, val):
        self.val = val
        self.both = 0

class XorLinkedList:
    def __init__(self):
        self.head = self.tail = None
        self.__nodes = []

    # O(1)
    def add(self, node):
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.both = id(node) ^ self.tail.both
            node.both = id(self.tail)
            self.tail = node

        self.__nodes.append(node)

    def get(self, index):
        prev_id = 0
        node = self.head
        for i in range(index):
            next_id = prev_id ^ node.both

            if next_id:
                prev_id = id(node)
                # Nothing in python that can get next node under next_id
                node = _get_obj(next_id)
            else:
                raise IndexError('Index out of range')
        return node

def _get_obj(id):
    return ctypes.cast(id, ctypes.py_object).value

if __name__ == '__main__':
    node = Node(1)
    node2 = Node(2)
    lst = XorLinkedList()

