class Node:
    def __init__(self, node_val, next_node = None, prev_node = None):
        self.node_val = node_val
        self.next_node = next_node
        self.prev_node = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def add_to_head(self, new_node_value):
        new_head_node = Node(new_node_value)
        old_head_node = self.head_node

        # If there already is an existing head node
        if self.head_node != None:
            # Set the new head node's next node to be the old head node
            new_head_node.next_node = old_head_node
            # Set the new head node's prev node to be None
            new_head_node.prev_node = None   
            # Set the old head node's prev node to be the new head node
            old_head_node.prev_node = new_head_node
            # Set the head node to be the new head 
            self.head_node = new_head_node

        # If there is no head node
        if self.head_node == None:
            # Set the node passed into the function as the new head node
            self.head_node = new_head_node
            # The new node will also be the new tail node (if there was nothing before)
            self.tail_node = new_head_node

        # Output the current state of the DLL
        self.output()
        print(f"{new_head_node.node_val} has been added")
        
    def add_to_tail(self, new_node_value):
        new_tail_node = Node(new_node_value)
        old_tail_node = self.tail_node

        # If there already is an existing tail node
        if self.tail_node != None:
            # Set the new tail's next node to be Nothing
            new_tail_node.next_node = None
            # Set the new tail's previous node to be the old tail node
            new_tail_node.prev_node = old_tail_node
            # Set the old tail node's next node to be the new tail
            old_tail_node.next_node = new_tail_node
            # Set the new tail node to be the tail node
            self.tail_node = new_tail_node

        # If there is no tail node
        if self.tail_node == None:
            # Set the node passed into the function as the new tail node
            self.tail_node = new_tail_node
            # The new node will also be the new head node (if there was nothing before)
            self.head_node = new_tail_node

        # Output the current state of the DLL
        self.output()
        print(f"{new_tail_node.node_val} has been added")

    def remove_node(self, node_value_to_remove):
        start_current_node = self.head_node # Tracks the current node we are from the start of the list
        rear_current_node = self.tail_node # Tracks the current node we are from the end of the list
        node_to_remove = None # Will be set to the node to remove when found

        # FINDING THE NODE TO REMOVE
        
        # If the value of the current node at the start of the list is the same as the value of the node we want to remove
        if start_current_node.node_val == node_value_to_remove:
            # Set the node to remove as the head node
            node_to_remove = self.head_node


        # If the value of the current node at the rear of the list is the same as the value of the node we want to remove
        if rear_current_node.node_val == node_value_to_remove:
            # Set the node to remove as the tail node
            node_to_remove = self.tail_node

        # Move the current nodes inwards (As they cannot be the head node or tail node)
        start_current_node = start_current_node.next_node
        rear_current_node = rear_current_node.prev_node
        
        # While we haven't found the node to remove
        while node_to_remove == None:

            # If the rear current node has reached the start of the list and the start current node reached the end of the list
            if rear_current_node == self.head_node and start_current_node == self.tail_node:
                print("End of list reached, node not found!")
                break
            
            # Check if the value of the start current node is the same as the value of the node we want to remove
            if start_current_node.node_val == node_value_to_remove:
                # Set the node to remove to be the current node
                node_to_remove = start_current_node

            # Check if the value of the rear current node is the same as the value of the node we want to remove
            if rear_current_node.node_val == node_value_to_remove:
                # Set the node to remove to be the current node
                node_to_remove = rear_current_node

            # Increment the start current node (moves inwards towards the rear node)
            start_current_node = start_current_node.next_node
            # Decrement the start current node (moves inwards towards the head node)
            rear_current_node = rear_current_node.prev_node

        # ----------------------------------------------------------------------------------
        # CHANGING THE POINTERS

        # In the case that the node was not found inside the DLL
        if node_to_remove == None:
            # Return nothing
            return None

        # If the node to remove is the tail node
        elif node_to_remove == self.tail_node:
            # Call the remove_tail method
            self.remove_tail()
            
        # If the node to remove is the head node
        elif node_to_remove == self.head_node:
            # Call the remove_head method
            self.remove_head()

        # Otherwise if the node to remove is in between the head node and the tail node 
        else:
            # Set the next node pointer of the node before the node we want to remove to point to what the node we want to remove is pointing to
            node_to_remove.prev_node.next_node = node_to_remove.next_node

            # Set the prev node pointer of the node after the node we want to remove to point to the previous node of the node we want to remove
            node_to_remove.next_node.prev_node = node_to_remove.prev_node

        # Output the current state of the list
        self.output()

    def remove_head(self):
        # Set the new head node to be node after the current (old) head node
        new_head_node = self.head_node.next_node

        # Set the previous node of the new head node to be nothing
        new_head_node.prev_node = None

        # Set the head node to be the new head node
        self.head_node = new_head_node

        # Display the message that the old head node has been removed
        print(f"{self.head_node.node_val} is now the new head node")

    def remove_tail(self):
        # Set the new tail node to be node before the current (old) tail node
        new_tail_node = self.tail_node.prev_node

        # Set the next node of the new tail node to be nothing
        new_tail_node.next_node = None

        # Set the tail node to be the new tail node
        self.tail_node = new_tail_node

        # Display the message that the old tail node has been removed
        print(f"{self.tail_node.node_val} is now the new tail node")    

    def output(self):
        current_node = self.head_node # Node used to iterate through the DLL
        list_of_items = [] # List to hold the values of all the nodes in the DLL

        # While we haven't reached the end of the DLL
        while current_node != None:
            # Append the value of the current node
            list_of_items.append(current_node.node_val)
            # Go to the next node
            current_node = current_node.next_node

        print(list_of_items)

    def iterative_reverse_dll(self):
        current_node = self.head_node # Start at the first node in the DLL

        while current_node: # Same as "while current_node != None"

            # Switch the values of the previous and next nodes of the current node
            current_node.prev_node, current_node.next_node = current_node.next_node, current_node.prev_node
            
            # Go to the next node (since prev and next node have swapped, prev_node goes to the next node)
            current_node = current_node.prev_node
        
        # Once current node is None, we have reached the end of the DLL, so swap the head and tail nodes
        self.head_node, self.tail_node = self.tail_node, self.head_node


        self.output()

my_dll = DoublyLinkedList()
my_dll.add_to_head(97)
my_dll.add_to_head(58)
my_dll.add_to_head(32)
my_dll.add_to_head(100)
my_dll.add_to_head(23)
my_dll.add_to_tail(62)
# my_dll.remove_node(62)
# my_dll.remove_node(23)
# my_dll.remove_node(32)
my_dll.iterative_reverse_dll()
