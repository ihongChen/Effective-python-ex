#! encoding=utf8

# 1. 因數分解
import time

def factorize(number):
    for i in range(1,number+1):
        if number % i == 0:
            yield i

numbers = [2139079,1214759,156637,1852285]
start = time.time()
for number in numbers:
    temp = list(factorize(number))
end = time.time()

print 'Took %.3f seconds'%(end-start)

# 2. 利用多執行緒執行因數分解

from threading import Thread

class FactorizeThread(Thread):
    def __init__(self,number):
        super(FactorizeThread,self).__init__()
        self.number = number

    def run(self):
        self.factors = list(factorize(self.number))

start = time.time()
threads = []
for number in numbers :
    thread = FactorizeThread(number)
    thread.start()
    threads.append(thread)

for thread in threads:
    thread.join()
end = time.time()
print 'Took %.3f seconds'%(end-start)

## 3. IO bound =>特別適合py多執行緒

import select

def slow_systemcall():
    select.select([],[],[],0.1)

start = time.time()

for _ in range(5):
    slow_systemcall()
end = time.time()
print 'Took %.3f seconds'%(end-start)


## 4. Thread in IO
start = time.time()
threads = []

for _ in range(5):
    thread = Thread(target=slow_systemcall)
    thread.start()
    threads.append(thread)

def compute_helicopter_location(index):
    print index

for i in range(5):
    compute_helicopter_location(i)
for thread in threads:
    thread.join()
end = time.time()

print 'Took %.3f seconds to finish.'%(end-start)
