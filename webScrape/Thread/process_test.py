# multiprocessing.py
from multiprocessing import Pool, Queue, Process
import os, time, random

def simple_test():
    print 'Process (%s) start...' % os.getpid()
    pid = os.fork()
    if pid==0:
        print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
    else:
        print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)



def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

def run_long_time_task():
    print 'Parent process %s.' % os.getpid()
    p = Pool()# default ,up to cpu number
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'
    
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())
def read(q):
     while True:
        value = q.get(True)
        print 'Get %s from queue.' % value
def run_communication():
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # write
    pw.start()
    # read:
    pr.start()
    # wait pw finish:
    pw.join()
    # pr'loop can't stop, so hand finish:
    pr.terminate()
if __name__=='__main__':
    #run_long_time_task()
    run_communication()
