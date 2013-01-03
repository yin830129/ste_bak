# simplesched.py
#
# A simple generator-based task scheduler

from collections import deque

def scheduler(taskqueue):
    while taskqueue:
        task = taskqueue.pop()
        try:
            next(task)               # Run to next yield
            taskqueue.appendleft(task)   # Reschedule
        except StopIteration:
            pass

# Example
if __name__ == '__main__':
    def countdown(n):
        while n > 0:
            print("countdown", n)
            n -= 1
            yield

    def countup(last):
        n = 0
        while n < last:
            print("countup", n)
            n += 1
            yield

    tasks = deque([countdown(10), countup(5)])
    scheduler(tasks)

        
