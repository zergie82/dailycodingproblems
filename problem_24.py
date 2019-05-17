'''
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.

Design a binary tree node class with the following methods:

    is_locked, which returns whether the node is locked
    lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
    unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.

You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.
'''


class Node:
    def __init__(self, data, parent=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.locked = False
        self.locked_childs_count = 0

    def __str__(self):
        return self.data

    def is_locked(self):
        return self.locked

    def lock(self):
        if self.is_locked():
            return False

        if not self.check_locks():
            return False

        self.locked = True

        cur = self.parent
        while cur:
            cur.locked_childs_count += 1
            cur = cur.parent
        return True

    def unlock(self):
        if not self.is_locked():
            return False

        if not self.check_locks():
            return False

        self.locked = False

        cur = self.parent
        while cur:
            cur.locked_childs_count -= 1
            cur = cur.parent
        return True

    def check_locks(self):
        if self.locked_childs_count > 0:
            return False

        cur = self.parent
        while cur:
            if cur.locked:
                return False
            cur = cur.parent
        return True

if __name__ == '__main__':
    root = Node('root')
    root.left = Node('root.left', root)
    root.right = Node('root.right', root)
    root.left.left = Node('root.left.left', root.left)
