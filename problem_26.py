'''
Given a singly linked list and an integer k, remove the kth last element from the list. k is guaranteed to be smaller than the length of the list.

The list is very long, so making more than one pass is prohibitively expensive.

Do this in constant space and in one pass.
'''

from collections import deque

class ListNode:
    def __init__(self, data, nextnode=None):
        self.data = data
        self.nextnode = nextnode

    def __str__(self):
        return self.data

class List:
    def __init__(self):
        self.head = None


def delete_from_list(l, k):
    trace = deque([], k + 1)

    node = l.head

    while node:
        trace.append(node)
        node = node.nextnode

    trace[0].nextnode = trace[2]

    return l


if __name__ == '__main__':
    my_list = List()
    my_list.head = ListNode(0, ListNode(1, ListNode(2, ListNode(3, ListNode(4)))))
