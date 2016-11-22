'''
P5. Add two linked lists from left to right
    e.g. 1->2->3 + 8->7 => 321+78 = 399
'''
from p1 import Node

def sum_linked_lists_backword(p1, p2):
    carry_over = 0
    head = Node(0)
    pointer = head
    digit = 0
    # until both linked lists exist, sum elements
    while p1 != None and p2 != None:
        sum_ = p1.val + p2.val + carry_over
        pointer.next = Node(sum_ % 10)
        pointer = pointer.next
        carry_over = sum_ / 10
        p1 = p1.next
        p2 = p2.next

    if p1 == None:
        while p2 != None:
            sum_ = p2.val + carry_over
            pointer.next = Node(sum_ % 10)
            pointer = pointer.next
            carry_over = sum_ / 10
            p2 = p2.next

    if p2 == None:
        while p1 != None:
            sum_ = p1.val + carry_over
            pointer.next = Node(sum_ % 10)
            pointer = pointer.next
            carry_over = sum_ / 10
            p1 = p1.next
    if carry_over > 0:
        pointer.next = Node(carry_over)
    return head.next

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(9)
    node5 = Node(8)
    node6 = Node(7)
    node1.next = node2
    node2.next = node3
    node4.next = node5
    node5.next = node6

    sum1 = sum_linked_lists_backword(node1,node4) # 321 + 789 = 1110
    sum2 = sum_linked_lists_backword(node1,node5) # 321 + 78 = 399
    sum1.traverse()
    sum2.traverse()
