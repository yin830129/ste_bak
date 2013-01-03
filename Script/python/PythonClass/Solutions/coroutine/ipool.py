# ipool.py
#

from multiprocessing.pool import Pool

class InlinedPool(Pool):
    def run_worker(self,func,result=None):
        try:
            w_func, w_args = func.send(result)
            self.apply_async(w_func,w_args,callback=lambda r: self.run_worker(func,r))
        except StopIteration:
            pass

import time
def add(x,y):
    time.sleep(5)
    return x+y

def example(n):
    while n > 0:
        r = yield add, (n,n)
        print r
        n -= 1
    print "Example Done"

if __name__ == '__main__':
    p = InlinedPool()
    p.run_worker(example(5))
    p.run_worker(example(10))
    p.run_worker(example(8))
    print "I'm done. Waiting around now"
    while True:
        time.sleep(1)



