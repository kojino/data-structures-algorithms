'''
P6. Add two linked lists from right to left
    e.g. 1->2->3 + 8->7 => 123+87 = 210
'''
import p1

class Node(p1.Node):
    def length(self):
        length = 1
        node = self
        while node != None:
            node = node.next
            length += 1
        return length

def pad_zeros(n,node):
    head = node
    for i in range(n):
        node0 = Node(0)
        node0.next = head
        head = node0
    return head

def sum_linked_lists_forward(p1,p2):
    p1_len = p1.length()
    p2_len = p2.length()
    if p1_len > p2_len:
        p2 = pad_zeros(p1_len - p2_len, p2)
    elif p2_len > p1_len:
        p1 = pad_zeros(p2_len - p1_len, p1)
    result,carry_over = sum_linked_lists_forward_helper(p1,p2)
    if carry_over > 0:
        new_node = Node(carry_over)
        new_node.next = result
        return new_node
    return result

def sum_linked_lists_forward_helper(p1,p2,):
    if p1 == None and p2 == None:
        return None,0
    else:
        result,carry_over = sum_linked_lists_forward_helper(p1.next,p2.next)
        sum_ = p1.val + p2.val + carry_over
        new_node = Node(sum_%10)
        new_node.next = result
        return new_node,sum_/10

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
    # sum1 = sum_linked_lists_forward(node1,node4) # 123 + 987 = 1110
    sum2 = sum_linked_lists_forward(node1,node5) # 123 + 87 = 210
    # sum1.traverse()
    sum2.traverse()
