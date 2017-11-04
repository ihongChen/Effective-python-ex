## multi-thread, Queue example

from threading import Lock
import Queue, time, threading, datetime  
import ipdb


class Job:    
     def __init__(self, name):    
             self.name = name    
     def do(self):    
             time.sleep(0.2)    
             print("\t[Info] Job({0}) is done!".format(self.name))  
  
que = Queue.Queue()  
for i in range(20):  
        que.put(Job(str(i+1)))  
  
print("\t[Info] Queue size={0}...".format(que.qsize()))  

  
def doJob(*args):  

    Que = args[0]
    
        # ipdb.set_trace()
    while Que.qsize() > 0:  
        job = Que.get()  
        job.do()
    # Que.task_done()  
  
# Open three threads  
# thd1 = threading.Thread(target=doJob, name='Thd1', args=(que,))  
# thd2 = threading.Thread(target=doJob, name='Thd2', args=(que,))  
# thd3 = threading.Thread(target=doJob, name='Thd3', args=(que,))  
  
# Start activity to digest Queue.  
st = datetime.datetime.now()  
# thd1.start()  
# thd2.start()  
# thd3.start()  
threads = []

for i in range(5):
    thread = threading.Thread(target=doJob,args=(que,))
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
    
# # Wait for all threads to terminate.  
# while thd1.is_alive() or thd2.is_alive() or thd3.is_alive():
#     print "waiting...one of thread is alive"
#     time.sleep(1)    
  
td = datetime.datetime.now() - st  
print("\t[Info] Spending time={0}!".format(td))
