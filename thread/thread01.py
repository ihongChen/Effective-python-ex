
import threading
import time


def job():
    """job
    """
    print('job {} start'.format(threading.current_thread()))
    time.sleep(0.1)
    print('job 1 finish')


def job2():
    """job2"""
    print('job {} start'.format(threading.current_thread()))
    time.sleep(0.1)
    print('job 2 finish')


if __name__ == '__main__':
    t1 = threading.Thread(target=job, name='j1')
    t2 = threading.Thread(target=job2, name='j2')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('main end')
