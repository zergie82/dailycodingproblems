'''
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. Given N, write a function that returns the number of unique ways you can climb the staircase. The order of the steps matters.
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

# O(2^n)
def staircase(n):
    if n <= 1:
        return 1

    return staircase(n-2) + staircase(n - 1)

def staircase3(n, X):
    if n < 0:
        return 0
    if n == 0:
        return 1
    else:
        return sum(staircase3(n - x, X) for x in X)

def staircase2(n):
    cache = [0 for _ in range(n+1)]
    cache[0] = 1

    for i in range(1, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[n]

def staircase4(n, X):
    cache = [0 for _ in range(n+1)]
    cache[0] = 1

    for i in range(1, n + 1):
        cache[i] = sum(cache[i-x] for x in X if i - x >= 0)

    return cache[n]

if __name__ == '__main__':
    print([(staircase(N), staircase2(N)) for N in range(5)])
    print([staircase3(N, {1, 3, 5}) for N in range(5)])
