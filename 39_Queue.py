# encoding : utf8
from queue import Queue
from threading import Thread
import time


# def consumer():
#     print('Consumer waiting...')
#     q.get()
#     print('Consumer done')


# def consumer2():
#     time.sleep(0.1)
#     q.get()
#     print('Consumer get 1')
#     q.get()
#     print('Consumer got 2')


def consumer3():
    print('Consumer Waiting')
    work = in_queue.get()
    print('Consumer Working...')
    print('Consumer done')
    in_queue.task_done()


if __name__ == '__main__':
    # ex1:
    # q = Queue()
    # td = Thread(target=consumer)
    # td.start()  # nothing to get from queue..pending
    # print('Producer putting')
    # q.put(object())
    # td.join()
    # print('Producer done')
    # ex2:
    # q = Queue(1)
    # td = Thread(target=consumer2)
    # td.start()

    # q.put(object())
    # print('Producer put 1')
    # q.put(object())
    # print('Producer put 2')
    # td.join()
    # print('Producer done...')
    # ex3
    # q = Queue()
    in_queue = Queue()
    Thread(target=consumer3).start()
    in_queue.put(object())
    print('Producer waiting')
    in_queue.join()
    print('Producer done')
