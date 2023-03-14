class Stack():
    def __init__(self, items_list = [] ):
        self.item_count = len(items_list)
        self.head_pointer = self.item_count - 1 # Set the head pointer (the pointer for the item at the top of the stack) (If it is empty, the pointer will be -1)
        self.items_list = items_list # If a list isn't passed into the instance when first being instantiated, by default, it will be empty.

    def push(self, item):
        # Increment the head pointer 
        self.head_pointer += 1
        # Add the item onto the stack
        self.items_list.append(item)

    def pop(self):
        # If the stack is empty, then don't do anything
        if self.isEmpty() == True:
            print("Unable to pop items when the stack is empty")
        else:
            print(f'{self.items_list[self.head_pointer]} has been popped off the stack')
            # Pop the item off the stack
            self.items_list.pop(self.head_pointer)
            # Decrement the head pointer
            self.head_pointer -= 1

    def isEmpty(self):
        # If the length of the list is greater than 0
        if len(self.items_list) > 0:
            # Then it isn't empty so return False
            return False
        # Otherwise return True
        return True

    def peek(self):
        if self.isEmpty() == False:
            print(f'The topmost element of the stack is {self.items_list[self.head_pointer]}')
        else:
            print("The stack is currently empty.")
    
    def size(self):
        print(f'There are {len(self.items_list)} items in the stack')

stack = Stack()
print(stack.items_list)
print("1", stack.head_pointer)

stack.push(50)
stack.push(48823)
print(stack.items_list)
print("2", stack.head_pointer)

stack.pop()
print(stack.items_list)
print("3", stack.head_pointer)

stack.pop()
stack.pop()
stack.push(50231)
stack.peek()
stack.size()