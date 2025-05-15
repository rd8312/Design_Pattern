# ref: https://shengyu7697.github.io/python-queue/

import queue
import time
import random
import threading

q = queue.Queue(10)

class Producer(threading.Thread):
    def __init__(self, thread_name):
        super(Producer, self).__init__(name=thread_name)

    def run(self):
        global q
        count = 1
        while True:
            if q.full():
                print('queue is full')
                pass
            else:
                msg = str(count)
                q.put(msg)
                print(self.name + ' put ' + msg + ', qsize: ' + str(q.qsize()))
                count=count+1     
            time.sleep(2)
            #time.sleep(random.random())

class Consumer(threading.Thread):
    def __init__(self, thread_name):
        super(Consumer, self).__init__(name=thread_name)

    def run(self):
        global q
        while True:
            if q.empty():
                print('queue is empty')
                pass
            else:
                msg=q.get()
                print(self.name + ' get ' + msg + ', qsize: ' + str(q.qsize()))
            time.sleep(1)

p = Producer('producer')
p.start()

c = Consumer('consumer')
c.start()