# multithread:helicopter simulation
from threading import Thread,Lock
from time import time
from select import select


start = time()
threads = []

def slow_systemcall():
    select([],[],[],0.1)

for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)

def compute_helicopter_location(index):
    # ...
    pass

for i in range(5):
    compute_helicopter_location(i)

for thread in threads:
    thread.join()

end=time()
print('Took %.3f seconds'%(end-start))
