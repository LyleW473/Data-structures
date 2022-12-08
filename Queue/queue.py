class Node:
    def __init__(self, node_val):
        self.node_val = node_val

class Queue:
    def __init__(self, max_size = None):
        self.size = 0 # # Is 0 there are no items in the queue
        self.head = None # Initially has no value as there are no items in the queue
        self.rear = None # Initially has no value as there are no items in the queue
        self.max_size = max_size

    def enqueue(self):
        pass

    def dequeue(self):
        pass

    def peek(self):
        pass

    def isEmpty(self):
        # If the queue has no items
        if self.size() == 0:
            return True
        # Otherwise
        else:
            return False

    def size(self):
        # Return the size of the queue
        return self.size


