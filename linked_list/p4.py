'''
P4. Delete a node from a linked list
'''


import p1

class Node(p1.Node):
    def delete_node(self):
        node = self
        if node == None or node.next == None:
            return False
        node.val = node.next.val
        node.next = node.next.next
        return True

if __name__ == "__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(1)
    node1.next = node2
    node2.next = node3
    node3.next = node4

    node2.delete_node()
    node1.traverse()
