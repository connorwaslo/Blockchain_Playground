from Node import Node


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, node=None):
        new_node = node
        new_node.assign_next(self.head)
        self.head = new_node

    def add_list(self, data_list=[]):
        for data in data_list:
            self.append(Node(data=data, next_node=None))

    def print(self):
        vals = []
        if self.head is not None:
            node = self.head
            while node is not None:
                # print(node.get())
                vals.insert(0, node.get())
                node = node.next()
        else:
            print("LinkedList is empty")

        print(vals)

