# implement the thread.Thread class to define a thread work class
# work for multi thread works

from Queue import *
from threading import *
from bt4 import BeautifulSoup
import time
import urllib


class Worker(Thread):

    work_count = 0
    def __init__(self,work_queue,result_queue,is_daemon,timeout =0 , **kwds):
        Thread.__init__(self,**kwds)
        self.id = work_count
        work_count++
        self.setDaemon(is_daemon)
        self.work_queue = work_queue
        self.result_queue = result_queue
        self.timeout = timeout

    def run(self):
        while True:
            try:
                callback,*args,**kwds = self.work_queue.get(self.timeout)
                result = callback(*args,**kwds)
                print "work[%2d] : %s" % (self.id,result)
            except Queue.empty:
                break
            except :
                print "thread may go wrong"


#WorkManger is a class to manage the work gather the work to do
class WorkManager():

    def __init__(self,work_count = 10,timeout = 0,is_daemon = bool('true')):
            self.work_queue = Queue()
            self.result_queue = Queue()
            self.works = []
            self.timeout = 0
            self.__init__workers__(work_count)

    def __init_workers__(self,work_count):
        for i in range(work_count):
            work = Work(self.work_queue,self.result_queue,is_daemon,self_timeout)
            self.works.append(work)
    
    def add_worker(callback,*arg,**kwds):
        self.work_queue.put((callback,*arg,**kwds))

    def start(self):
        for work in works:
            work.start()
