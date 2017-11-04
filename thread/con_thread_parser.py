# concurrency parsing

## stackoverflow: issue

# I am opening a file which has 100,000 url's. 
# I need to send an http request to each url and print the status code. 
# I am using Python 2.6, and so far looked at the many confusing ways Python implements threading/concurrency. 
# I have even looked at the python concurrence library, but cannot figure out how to write this program correctly. 
# Has anyone come across a similar problem? 
# I guess generally I need to know how to perform thousands of tasks in Python as fast as possible - I suppose that means 'concurrently'.
#

from urlparse import urlparse
from threading import Thread
import httplib, sys
from Queue import Queue

concurrent = 200

def doWork():
    while True:
        url = q.get()
        status, url = getStatus(url)
        doSomethingWithResult(status, url)
        q.task_done()

def getStatus(ourl):
    try:
        url = urlparse(ourl)
        conn = httplib.HTTPConnection(url.netloc)   
        conn.request("HEAD", url.path)
        res = conn.getresponse()
        return res.status, ourl
    except:
        return "error", ourl

def doSomethingWithResult(status, url):
    print status, url

q = Queue(concurrent * 2)

for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    for url in open('urllist.txt'):
        q.put(url.strip())
    q.join()
except KeyboardInterrupt:
    sys.exit(1)