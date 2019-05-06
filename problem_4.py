'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

def missing(a):
    a = set(a)
    for i in range(1, len(a)+2):
        if i not in a:
            return i

# O(n) time and space
def missing2(a):
    a = set(a)
    i = 1
    while i in a:
        i += 1
    return i

# O(n) time, space swap only
def missing3(a):
    if not a:
        return 1

    for i, num in enumerate(a):
        while i+1 != a[i] and 0 < a[i] <= len(a):
            v = a[i]
            a[i], a[v - 1] = a[v - 1], a[i]
            if a[i] == a[v -1 ]:
                break

    for i, num in enumerate(a, 1):
        if i != num:
            return i

    return len(a) + 1

if __name__ == "__main__":
    a = (
        [3, 4, -1, 1],
        [1, 2, 0]
    )
    print([missing(x) for x in a])
    print([missing2(x) for x in a])
    print([missing3(x) for x in a])
