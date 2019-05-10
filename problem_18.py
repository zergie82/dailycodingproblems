'''
Given an array of integers and a number k, where 1 <= k <= length of the array, compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8], since:

10 = max(10, 5, 2)
7 = max(5, 2, 7)
8 = max(2, 7, 8)
8 = max(7, 8, 7)
Do this in O(n) time and O(k) space. You can modify the input array in-place and you do not need to store the results. You can simply print them out as you compute them.
'''

def maximums(arr, k):
    if not 1 <= k <= len(arr):
        return 0

    maxes = []

    for index in range(0, len(arr) - k + 1):
        maxx = 0
        maxx = max(arr[index:index + k])
        maxes.append(maxx)

    return maxes

from collections import deque

def max1(arr, k):
    q = deque()
    for i in range(k):
        while q and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)
        print(list(q))

    for i in range(k, len(arr)):
        print(arr[q[0]])
        while q and q[0] <= i - k:
            q.popleft()
        while q and arr[i] >= arr[q[-1]]:
            q.pop()
        q.append(i)
    print(arr[q[0]])


if __name__ == '__main__':
    arr = [10, 5, 2, 7, 8, 7]
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
    k = 3

