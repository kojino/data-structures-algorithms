'''
P3. Get the kth to last element from a linked list
'''


import p1

class Node(p1.Node):
    def kth_to_last(self,k):
        if k < 0:
            return None
        p1 = self
        p2 = self
        i = -1
        while p1 != None:
            p1 = p1.next
            if i < k:
                i += 1
            else:
                p2 = p2.next
        if i == k:
            return p2.val
        else:
            return None

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    print node1.kth_to_last(2)
    print node1.kth_to_last(-10)
