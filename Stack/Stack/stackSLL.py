class Node:
    def __init__(self, node_val, next_node = None):
        self.node_val = node_val
        self.next_node = next_node

class Stack:
    def __init__(self, max_size = 10):
        self.max_size = max_size # Declares the maximum size of the stack
        self.top_item = None # There is no top item if the stack is empty
        self.size = 0 # Stack starts with 0 items

    def push(self):
        pass

    def pop(self):
        pass

    def peek(self):
        pass

    def isFull(self):
        return self.size == self.max_size

    def isEmpty(self):
        return self.size == 0

    def output(self):
        pass

myStack = Stack()
print(myStack.isEmpty())
print(myStack.isFull())
