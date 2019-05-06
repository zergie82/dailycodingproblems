'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

from functools import reduce

# O(n)
def gen_array(a):
    return [reduce(lambda x,y: x * y, a[:i] + a[i+1:]) for i in range(len(a))]

# O(n)
def gen_array2(a):
    # Generate prefix/suffix lists
    prefix = []
    for num in a:
        if prefix:
            prefix.append(prefix[-1] * num)
        else:
            prefix.append(num)

    suffix = []
    for num in reversed(a):
        if suffix:
            suffix.append(suffix[-1] * num)
        else:
            suffix.append(num)
    suffix = list(reversed(suffix))

    result = []

    for i in range(len(a)):
        if i == 0:
            result.append(suffix[i + 1])
        elif i == len(a) - 1:
            result.append(prefix[i -1])
        else:
            result.append(prefix[i - 1] * suffix[i + 1])
    return result

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    print(gen_array(a))
    print(gen_array2(a))
