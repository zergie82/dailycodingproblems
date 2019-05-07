'''
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.
'''

from time import sleep, time
import threading

class Scheduler:
    def __init__(self):
        self.fns = []
        t = threading.Thread(target=self.poll)
        t.start()

    def poll(self):
        while True:
            now = time() * 1000
            for fn, due in self.fns:
                if now > due:
                    fn()
            self.fns = [(fn, due) for (fn, due) in self.fns if due > now]
            sleep(0.01)

    def delay(self, f, n):
        self.fns.append((f, time() * 1000 + n))

def scheduler(f, ms):
    time_in_s = ms / 1000

    sleep(time_in_s)
    f()
    # return f()

if __name__ == '__main__':
    def f(): print('Hello!')
    ms =10000

    scheduler(f, ms)
