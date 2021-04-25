#COMBINE TWO QUEUES TOGETHER AND FORM ONE NEW QUEUE
from collections import deque

class Queue(object):
    def __init__(self):
        self.queue1 = deque([])
        self.queue2 = deque([])
        self.queue3 = deque([])

    def push_to_queue1(self,data):
        self.queue1.append(data)

    def push_to_queue2(self,data):
        self.queue2.append(data)

    def create(self):
        for i in range(len(self.queue1)):
            self.queue3.append(self.queue1[i])
            self.queue3.append(self.queue2[i])
    
    def print(self):
        return self.queue3
    
queue = Queue()
queue.push_to_queue1('a')
queue.push_to_queue1('c')
queue.push_to_queue1('e')
queue.push_to_queue2('b')
queue.push_to_queue2('d')
queue.push_to_queue2('f')
queue.create()
print(queue.print())

