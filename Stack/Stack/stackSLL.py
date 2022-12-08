class Node:
    def __init__(self, node_val, next_node = None):
        self.node_val = node_val
        self.next_node = next_node

class Stack:
    def __init__(self, max_size = 10):
        self.max_size = max_size # Declares the maximum size of the stack
        self.top_item = None # There is no top item if the stack is empty
        self.size = 0 # Stack starts with 0 items

    def push(self, item_value):
        
        # If the stack is: (Empty and not full) or (Not empty and not full)
        if (self.isEmpty() == True and self.isFull() == False) or (self.isEmpty() == False and self.isFull() == False):

            # Create a new node with the item value
            new_item = Node(item_value)

            # In the case that its (Not empty and not full), we also need to set the new item's next node to be the previous top item
            if self.isEmpty() == False and self.isFull() == False:
                # Set the new items next node to be the previous top item
                new_item.next_node = self.top_item

            # Set the top item as the new item
            self.top_item = new_item
            # Increment the size of the stack
            self.size += 1
            # Output all of the items inside of the stack
            self.output()
            print(f"{new_item.node_val} has been pushed onto the stack!")
            
        # If the stack is: (Not empty and full)
        elif (self.isEmpty() == False and self.isFull() == True):
            print("Cannot push items onto a full stack!")
        

    def pop(self):
        pass

    def peek(self):
        pass

    def isFull(self):
        return self.size == self.max_size

    def isEmpty(self):
        return self.size == 0

    def output(self):
        current_node = self.top_item # Start at the start of the queue
        output_list = [] # List to hold the values of each item in the queue

        while current_node: # Same as "while current_node != None"
            # Append the current node's value to the output list
            output_list.append(current_node.node_val)
            # Go to the next node
            current_node = current_node.next_node

        # Print the output list
        print(output_list)

myStack = Stack()
print(myStack.isEmpty())
print(myStack.isFull())

for i in range(1, 12):
    myStack.push(i)