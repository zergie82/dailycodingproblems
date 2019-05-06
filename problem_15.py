'''
Given a stream of elements too large to store in memory, pick a random element from the stream with uniform probability.
'''

import random

def pick(stream):
    el = None
    sample = []
    sample_size = 1
    for index, value in enumerate(stream):
        if index < sample_size:
            sample.append(value)
        else:
            r = random.randint(0, index)
            if r < sample_size:
                sample[r] = value

    print(sample)



if __name__ == '__main__':
    stream = [74, 99, 10, 85, 81, 91, 58, 11, 95, 14, 34, 25, 8, 2, 78, 93, 64, 66, 8, 36]

    pick(stream)
