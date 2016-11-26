'''
Write a program to sort a stack in ascending order (with biggest items on top).
You may use at most one additional stack to hold items,
but you may not copy the elements into any other data structure (suchasan array).
The stack supports the following operations: push, pop, peek, and isEmpty.
'''
from p0 import Stack

def sort_stack(stack):
    result = Stack()
    while stack.size() > 0:
        # pop the top el from stack
        el = stack.pop()
        # until the top el is smaller than el
        num_popped_from_result = 0
        while result.peak() > el:
            # pop els from result and push them to stack
            stack.push(result.pop())
            num_popped_from_result += 1
        # push el
        result.push(el)
        # push els popped back to result
        for i in range(num_popped_from_result):
            result.push(stack.pop())
    return result

if __name__ == "__main__":
    stack = Stack()
    stack.push(4)
    stack.push(5)
    stack.push(2)
    stack.push(1)
    stack = sort_stack(stack)
    print stack.stack
