'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
'''
from bisect import bisect_left

def check(l, k):
    if [x for x in l if (k - x) in l]:
        return True
    else:
        return False

# O(n²)
def check2(l, k):
    for i in range(len(l)):
        for j in range(len(l)):
            if i != j and l[i] + l[j] == k: 
                    return True
    return False

# O(n)
def check3(l, k):
    seen = set()
    for num in l:
        if k - num in seen:
            return True
        seen.add(num)
    return False

# O(nlogn)
def check4(l, k):
    l.sort()

    for i in range(len(l)):
        target = k - l[i]
        j = binary_search(l, target)

        if j == -1:
            continue
        elif j != i:
            return True
        elif j + 1 < len(l) and l[j + 1] == target:
            return True
        elif j - 1 >=0 and l[j - 1] == target:
            return True
    return False

def binary_search(l, target):
    i = bisect_left(l, target)
    if 0 <= i <= len(l) and l[i] == target:
        return i
    return -1

if __name__ == "__main__":
    l = [10, 15, 3, 7]
    k = 17
    print(check(l, k))
    print(check2(l, k))
    print(check3(l, k))
    print(check4(l, k))
