class Node:
    def __init__(self, node_val):
        self.node_val = node_val

class Queue:
    def __init__(self, max_size = None):
        self.size = 0 # # Is 0 there are no items in the queue
        self.head = None # Initially has no value as there are no items in the queue
        self.rear = None # Initially has no value as there are no items in the queue
        self.max_size = max_size

    def enqueue(self, new_item):
        # If the queue has no declared max size, or the size of the queue is not max_size.
        if self.isFull() == False:
            pass
        # Otherwise, if the queue is full
        else:
            print("Cannot enqueue to a full list")

    def dequeue(self):
        pass

    def peek(self):
        pass

    def isEmpty(self):
        # If the queue has no items
        if self.size == 0:
            return True
        # Otherwise
        else:
            return False

    def isFull(self):
        # If the queue has no declared max size
        if self.max_size == None:
            return False
        # Elif the size of the list is equal to the max size
        elif self.size == self.max_size:
            return True
        # Otherwise
        else:
            return False

    def size(self):
        # Return the size of the queue
        return self.size


myQueue = Queue()
myQueue.enqueue("hehre")
