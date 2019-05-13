'''
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.
'''


def max_rooms(intervals):
    starts = sorted(start for start, end in intervals)
    ends = sorted(end for start, end in intervals)

    cmax = 0
    coverlapp = 0
    i, j = 0, 0

    while i < len(intervals) and j < len(intervals):
        if starts[i] < ends[j]:
            coverlapp += 1
            cmax = max(cmax, coverlapp)
            i += 1
        else:
            coverlapp -= 1
            j += 1
    return cmax

if __name__ == '__main__':
    intervals = [(30, 75), (0, 50), (60,150)]
