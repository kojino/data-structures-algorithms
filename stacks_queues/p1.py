'''
P1. Implement a queue
'''
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,val):
        self.queue.insert(0,val)

    def dequeue(self):
        return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size == 0
