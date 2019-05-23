'''
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1) space.

For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.

Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.
'''

def capacity(arr):
    units = 0
    max_i = arr.index(max(arr))

    left_max = arr[0]
    for i in arr[1:max_i]:
        units += left_max - i
        left_max = max(left_max, i)

    right_max = arr[-1]
    for i in arr[-2:max_i:-1]:
        units += right_max - i
        right_max = max(right_max, i)

    return units


if __name__ == '__main__':
    lmap = [2, 1, 2]
    lmap2 = [3, 0, 1, 3, 0, 5]

    assert capacity(lmap) == 1
    assert capacity(lmap2) == 8
