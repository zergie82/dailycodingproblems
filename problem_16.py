'''
You run an e-commerce website and want to record the last N order ids in a log. Implement a data structure to accomplish this, with the following API:

    record(order_id): adds the order_id to the log
    get_last(i): gets the ith last element from the log. i is guaranteed to be smaller than or equal to N.

You should be as efficient with time and space as possible.
'''

from collections import deque

class Log:
    def __init__(self, order_id, size):
        self.log = deque([order_id,], size)
        self.size = size

    def __str__(self):
        return f'{list(self.log)}'

    def record(self, order_id):
        self.log.append(order_id)

    def get_last(self, i):
        if i <= self.size:
            return self.log[-i]
        else:
            return None
