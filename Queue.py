from collections import deque

class Queue(object):
    def __init__(self):
        self.queue = deque([])
    
    # push(x) -- Push element x onto queue
    def push(self,data):
        self.queue.append(data)
    
    # pop() -- Removes the element first element of queue.
    def pop(self):
        self.queue.pop()

    # top() -- Get the top element.
    def top(self):
        return self.queue[0]

    # get() -- Get all the elements in the queue
    def get(self):
        return self.queue

    # empty() -- Return whether the queue is empty.
    def empty(self):
        return not self.queue

queue = Queue()
queue.push('Phoo')
queue.push('Pyae')
queue.push('Pyae')
queue.push('Linn')
print('all elements in queue')
print(queue.get())
print('first element of queue')
print(queue.top())
queue.pop()
print('elements in queue after pop',queue.get())
