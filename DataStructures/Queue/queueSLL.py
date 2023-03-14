class Node:
    def __init__(self, node_val, next_node = None):
        self.node_val = node_val
        self.next_node = next_node

class Queue:
    def __init__(self, max_size = None):
        self.size = 0 # # Is 0 there are no items in the queue
        self.head = None # Initially has no value as there are no items in the queue
        self.rear = None # Initially has no value as there are no items in the queue
        self.max_size = max_size

    def enqueue(self, new_item_value):
        # If the queue has no declared max size, or the size of the queue is not max_size.
        if self.isFull() == False:
            # Create a node with the new item value
            new_item = Node(new_item_value)

            # If the queue is empty
            if self.isEmpty() == True:
                # The new node will become the head and rear of the queue  
                self.head, self.rear = new_item, new_item

            # If the queue is not empty
            if self.isEmpty() == False:
                # Set the old rear node's next node to be the new item
                self.rear.next_node = new_item
                # Set the rear node as the new item
                self.rear = new_item

            # Increment the size of the queue
            self.size += 1 

            # Print all of the items inside the queue
            self.output()

        # Otherwise, if the queue is full
        else:
            print("Cannot enqueue to a full queue!")

    def dequeue(self):
        # If the queue is empty
        if self.isEmpty() == True:
            print("Cannot dequeue from an empty queue!")
        
        # If the queue isn't empty 
        else:
            # Start from the beginning of the queue
            current_node = self.head

            # While we haven't reached the rear of the queue
            while current_node != self.rear:
                # Set the previous node as the current node
                prev_node = current_node
                # Go to the next node
                current_node = current_node.next_node

            # If the item we want to dequeue is the only item in the queue
            if current_node == self.head and current_node == self.rear:
                # Set the head and rear of the queue to be None
                self.head = None
                self.rear = None

            # If this is any other item
            else:
                # Set the next node of previous node of the old rear node to be None
                prev_node.next_node = None
                # Set the rear node to be the previous node
                self.rear = prev_node
        
            # Decrement the size of the queue
            self.size -= 1

            # Print all of the items in the queue, and what item was removed
            self.output()
            print(f"{current_node.node_val} has been removed from the queue!")

    def peek(self):
        # If the queue is empty
        if self.isEmpty() == True:
            return "Cannot look at the first item in the queue when the queue is empty!"
        # Otherwise
        else:
            # Return the value of the first item in the queue
            return self.head.node_val

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
        # Elif the size of the queue is equal to the max size
        elif self.size == self.max_size:
            return True
        # Otherwise
        else:
            return False

    def size(self):
        # Return the size of the queue
        return self.size

    def output(self):
        current_node = self.head # Start at the start of the queue
        output_list = [] # List to hold the values of each item in the queue

        while current_node: # Same as "while current_node != None"
            # Append the current node's value to the output list
            output_list.append(current_node.node_val)
            # Go to the next node
            current_node = current_node.next_node

        # Print the output list
        print(output_list)


myQueue = Queue(3)
myQueue.enqueue("hello")
myQueue.enqueue(23)
myQueue.enqueue("world")
myQueue.enqueue(53)
print(f"The first item in myQueue is {myQueue.peek()}")
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
myQueue.dequeue()
myQueue.enqueue(97)
myQueue.enqueue("!")
print(f"The first item in myQueue is {myQueue.peek()}")
myQueue.dequeue()
myQueue.dequeue()
print(myQueue.peek())