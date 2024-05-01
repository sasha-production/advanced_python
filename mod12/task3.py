from threading import Semaphore, Thread
import time
import signal

sem: Semaphore = Semaphore()
end_flag = False
sem: Semaphore = Semaphore()


def fun1():
    global end_flag
    while not end_flag:
        sem.acquire()
        print(1)
        sem.release()
        time.sleep(0.25)


def fun2():
    global end_flag
    while not end_flag:
        sem.acquire()
        print(2)
        sem.release()
        time.sleep(0.25)

def handle_interrupt(signum, frame):
    global end_flag
    end_flag = True
    print('\nreceived interrupt')

    
t1: Thread = Thread(target=fun1)
t2: Thread = Thread(target=fun2)

signal.signal(signal.SIGINT, handle_interrupt)
t1.start()
t2.start()

t1.join()
t2.join()