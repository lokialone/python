import threading
import time

threadLock = threading.Lock()

class myThread (threading.Thread):
    
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print "Starting " + self.name
        
        print_time(self.name, self.counter, 5)
        print "Exiting " + self.name
        
 
def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        threadLock.acquire()
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1
        threadLock.release()

if __name__ == '__main__':
    # create thread
    threads = []
    thread1 = myThread(1, "Thread-1", 1)
    thread2 = myThread(2, "Thread-2", 2)
    # lanch thread
    thread1.start()
    thread2.start()

    threads.append(thread1)
    threads.append(thread2)
    
    # 
    for t in threads:
        t.join()
    print "Exiting Main Thread"
