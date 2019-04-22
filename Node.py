class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def assign_next(self, next=None):
        self.next_node = next

    def next(self):
        if self.next_node is None:
            return None

        return self.next_node

    def get(self):
        return self.data
