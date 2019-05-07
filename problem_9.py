'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

def largest_non_adj(a):
    if not a:
        return 0

    return max(
        largest_non_adj(a[1:]),
        a[0] + largest_non_adj(a[2:])
    )

def largest_non_adj2(arr):
    if len(arr) <= 2:
        return max(0, max(arr))

    cache = [0 for _ in arr]
    cache[0] = max(0, arr[0])
    cache[1] = max(cache[0], arr[1])

    for i in range(2, len(arr)):
        num = arr[i]
        cache[i] = max(num + cache[i - 2], cache[i - 1])
    return cache[-1]


if __name__ == '__main__':
    lst = [2, 4, 6, 2, 5]
    lst2 = [5, 1, 1, 5]

    print(largest_non_adj(lst), largest_non_adj(lst2))
    print(largest_non_adj2(lst), largest_non_adj2(lst2))

