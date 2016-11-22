'''
P0. Implement a stack
'''
class Stack:
    def __init__(self):
        self.stack = []

    def pop(self):
        return self.stack.pop()

    def push(self,val):
        return self.stack.append(val)

    def peak(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size == 0
