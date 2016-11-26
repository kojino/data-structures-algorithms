'''
Implement a queue with two stacks
'''

from p0 import Stack

class QueueWithStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self,el):
        self.stack1.push(el)

    def dequeue(self):
        if not self.stack2.size > 0:
            self.move_content()
        return self.stack2.pop()

    def move_content(self):
        while self.stack1.size > 0:
            self.stack2.push(self.stack1.pop())
