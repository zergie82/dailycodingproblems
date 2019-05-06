'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.


{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}

mapping = dict(zip(string.ascii_lowercase, map(str, range(1, 27))))
'''
import string

def helper(message, k, memo):
    if k == 0:
        return 1

    s = len(message) - k

    if message[s] == '0':
        return 0

    if memo[k] != None:
        return memo[k]

    result = helper(message, k - 1, memo)
    if k >= 2 and int(message[s:s+2]) <= 26:
        result += helper(message, k - 2, memo)
    memo[k] = result
    return result

def count(message):
    memo = [None] * (len(message) + 1)
    return helper(message, len(message), memo)

# O(2^n)
def count2(message):
    if message.startswith('0'):
        return 0
    if len(message) <= 1:
        return 1

    total = 0

    if int(message[:2]) <= 26:
        total += count2(message[2:])

    total += count2(message[1:])

    return total
