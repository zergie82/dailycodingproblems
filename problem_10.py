'''
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''

from time import sleep


def scheduler(f, ms):
    time_in_s = ms / 1000

    sleep(time_in_s)
    f()
    # return f()

if __name__ == '__main__':
    def f(): print('Hello!')
    ms =10000

    scheduler(f, ms)
