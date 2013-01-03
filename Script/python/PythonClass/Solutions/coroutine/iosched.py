# iosched.py
#
# A simple coroutine based task scheduler

import select
import socket
import errno
from collections import deque


# ----------------------------------------------------------------------
# Scheduler traps.  These objects are returned by yield statements in
# coroutines to initiate actions in the scheduler (e.g., I/O waiting).
#
# The critical method is the trap() method which receives an instance
# of the scheduler and the associated coroutine.  The finish() method
# is used upon the completion of whatever waiting event was requested.
# ----------------------------------------------------------------------

class SchedulerTrap:
    '''
    Class representing a general scheduler trap.
    '''
    def trap(self,sched,task):
        '''
        Method triggered when a task yields to scheduler control.
        '''
        pass

    def finish(self,sched):
        '''
        Method triggered upon completion of the trap.
        '''
        pass

# ----------------------------------------------------------------------
# Socket Operations
# ----------------------------------------------------------------------

class RecvWait(SchedulerTrap):
    '''
    Task wants to read data on socket
    '''
    def __init__(self,sock,maxlen):
        self.sock = sock
        self.fileno = sock.fileno()
        self.maxlen = maxlen
    
    def trap(self,sched,task):
        self.task = task
        # Immediately try to read data with hope that there is something there
        try:
            data = self.sock.recv(self.maxlen)
            sched.reschedule(task,data)
        except socket.error as e:
            if e.errno == errno.EWOULDBLOCK:
                sched.wait_for_read(self.fileno,self)
            else:
                raise

    def finish(self,sched):
        data = self.sock.recv(self.maxlen)
        sched.reschedule(self.task,data)

class SendWait(SchedulerTrap):
    '''
    Task wants to send data on socket
    '''
    def __init__(self,sock,data):
        self.sock = sock
        self.fileno = sock.fileno()
        self.data = data
    
    def trap(self,sched,task):
        self.task = task
        # Immediately try to send data with hope that it can be accepted
        try:
            nsent = self.sock.send(self.data)
            sched.reschedule(task,nsent)
        except socket.error as e:
            if e.errno == errno.EWOULDBLOCK:
                sched.wait_for_write(self.fileno,self)
            else:
                raise

    def finish(self,sched):
        nsent = self.sock.send(self.data)
        sched.reschedule(self.task,nsent)

class AcceptWait(SchedulerTrap):
    '''
    Task wants to accept a client connection
    '''
    def __init__(self,sock):
        self.sock = sock
        self.fileno = sock.fileno()
    
    def trap(self,sched,task):
        self.task = task
        sched.wait_for_read(self.fileno,self)

    def finish(self,sched):
        c_addr = self.sock.accept()
        sched.reschedule(self.task,c_addr)

class ConnectWait(SchedulerTrap):
    '''
    Task wants to accept a client connection
    '''
    def __init__(self,sock,addr):
        self.sock = sock
        self.fileno = sock.fileno()
        self.addr = addr
    
    def trap(self,sched,task):
        self.task = task
        try:
            self.sock.connect(self.addr)
        except socket.error as e:
            if e.errno == errno.EWOULDBLOCK:
                sched.wait_for_write(self.fileno,self)
            else:
                raise

    def finish(self,sched):
        sched.reschedule(self.task)

class SocketWrapper:
    '''
    Class around a socket object for async handling by the scheduler.
    '''
    def __init__(self,sock):
        self._sock = sock
        self._sock.setblocking(False)
    def accept(self):
        return AcceptWait(self._sock)
    def connect(self,addr):
        return ConnectWait(self._sock,addr)
    def recv(self,maxlen):
        return RecvWait(self._sock,maxlen)
    def send(self,data):
        return SendWait(self._sock,data)
    def __getattr__(self,name):
        '''
        Delegate other socket operations to the underlying socket object.
        '''
        return getattr(self._sock,name)
        
# ----------------------------------------------------------------------
# Task scheduler
# ----------------------------------------------------------------------
class Scheduler:
    def __init__(self):
        self._task_queue = deque()
        self._waiting_to_read = {}
        self._waiting_to_write = {}
        self.ntasks = 0
        
    def new_task(self,task):
        '''
        Add a new task to the task queue.
        '''
        self._task_queue.append((task,None))
        self.ntasks += 1

    def reschedule(self,task,result=None):
        '''
        Reschedule a task for running.
        '''
        self._task_queue.append((task,result))

    def wait_for_read(self,fd,trap):
        '''
        Add a task to the waiting to read pool.
        '''
        assert fd not in self._waiting_to_read
        self._waiting_to_read[fd] = trap

    def wait_to_write(self,fd,trap):
        '''
        Add a task to the waiting to write pool
        '''
        assert fd not in self._waiting_to_write
        self._waiting_to_write[fd] = trap

    def poll_for_io(self):
        '''
        Poll for I/O for all waiting tasks.
        '''
        readers, writers, _ = select.select(self._waiting_to_read,self._waiting_to_write,[])
        for r in readers:
            self._waiting_to_read.pop(r).finish(self)
        for w in writers:
            self._waiting_to_write.pop(w).finish(self)

    def run(self):
        while self.ntasks:
            while not self._task_queue:
                self.poll_for_io()
            task,result = self._task_queue.popleft()
            # Run the task to the next yield
            try:
                action = task.send(result)
                if action:
                    action.trap(self,task)
                else:
                    self.reschedule(task)
            except StopIteration:
                self.ntasks -= 1
            except Exception as e:
                print("Task crashed: %s" % e)

if __name__ == '__main__':

    # Example:  A coroutine-based echo server
    def echo_client(client_sock, addr):
        print "Got a connection from", addr
        while True:
            data = yield client_sock.recv(1024)
            if not data:
                break
            while data:
                nsent = yield client_sock.send(data)
                data = data[nsent:]
        print "Connection closed"
        client_sock.close()

    def echo_server(server_addr,sched):
        sock = SocketWrapper(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        sock.bind(server_addr)
        sock.listen(1)
        print "Server listing on", server_addr
        while True:
            client_sock, addr = yield sock.accept()
            sched.new_task(echo_client(SocketWrapper(client_sock),addr))

    sched = Scheduler()
    sched.new_task(echo_server(("",16000), sched))
    sched.run()




        





