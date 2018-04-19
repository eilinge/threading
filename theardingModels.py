#_*_utf-8_*_
'''
import threading
import time

def worker(num):
    time.sleep(1)
    print(num)
    return

for i in range(10):
    t = threading.Thread(target=worker, args=(i, ), name='t.%d'%i)
    t.start()

import threading
import time

class MyThread(threading.Thread):
    def __init__(self,num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print('running on number:%s'%self.num)

        time.sleep(2)

if __name__=='__main__':
    t1 = MyThread(1)
    t2 = MyThread(2)
    t1.start()
    t2.start()

import threading
import time

class MyThread(threading.Thread):
    def __init__(self,x):
        threading.Thread.__init__(self)
        self.x = x

    def run(self):

        print('running time %s'%self.x)

        time.sleep(2)

if __name__=='__main__':
    t1 = MyThread(2)
    t2 = MyThread(5)
    t3 = MyThread(4)
    t1.start()
    t1.setName('lala')
    t2.setName('lalalala')
    t3.start()
    t2.start()

import threading
import time

globals_num = 0

lock = threading.RLock()

def Func():
    lock.acquire()
    global globals_num
    globals_num += 1
    time.sleep(1)
    print(globals_num)
    lock.release()

for i in range(10):
    t = threading.Thread(target=Func)
    t.start()

from multiprocessing import Process
 
def func(name):
    print('hello', name) 
 
if __name__ == "__main__":
    p = Process(target=func,args=('zhangyanlin',))
    p.start()
    p.join()  # 等待进程执行完毕
'''
import os
import signal
import time

def my_term(a,b):
    print('收到sigtrem信号')
signal.signal(signal.SIGTERM,my_term)

def my_fpe(a,b):
    print('收到fpe信号')
    
signal.signal(signal.SIGFPE,my_fpe)
while 1:
    print('我是进程id',os.getpid())
    time.sleep(1)






















