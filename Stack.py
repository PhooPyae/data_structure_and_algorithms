from collections import deque

class Stack(object):
    def __init__(self):
        self.stack = deque([])
    
    def push(self,data):
        self.stack.append(data)
        for i in range(0,len(self.stack)-1):
            self.stack.append(self.stack.popleft())

    def pop(self):
        self.stack.popleft()
    
    def top(self):
        return self.stack[0]
    
    def get(self):
        return self.stack
    
    def empty(self):
        return not self.stack
    
stack = Stack()
stack.push('phoo')
stack.push('pyae')
stack.push('pyae')
stack.push('linn')
print('top element',stack.top())
print('all elements',stack.get())
print('pop')
stack.pop()
print('after pop',stack.get())