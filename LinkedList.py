class Node(object):
    def __init__(self,data):
        self.data = data #contains the data
        self.next = None #contains the reference to the next node

class LinkedList(object):
    def __init__(self):
        self.head = None

    def add_node(self,new_data):
        new_node = Node(new_data) #create a new node
        new_node.next = self.head #set the current to the new one
        self.head = new_node #link the new node to the previous node

    def list_print(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

linklist = LinkedList()
linklist.add_node(1)
linklist.add_node(2)
linklist.add_node(3)

linklist.list_print()