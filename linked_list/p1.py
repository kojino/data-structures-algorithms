'''
P1. Traverse a linked list
'''
import p0

class Node(p0.Node):
    def traverse(self):
        node = self
        while node != None:
            print node.val
            node = node.next

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    node1.traverse()
