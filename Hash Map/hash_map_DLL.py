from hash_map import HashMap

class Node:
    def __init__(self, node_val, next_node = None, prev_node = None):
        self.node_val = node_val
        self.next_node = next_node
        self.prev_node = prev_node

class DoublyLinkedList:
    def __init__(self, max_size = None):
        self.head_node = None
        self.tail_node = None
        self.size = 0
        self.max_size = max_size

    def add_to_head(self, new_node_value):
        new_head_node = Node(new_node_value)
        old_head_node = self.head_node

        # If the size of the DLL hasn't reached the max size
        if self.size != self.max_size:

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

            # Increment the size of the DLL
            self.size += 1

            # Output the current state of the DLL
            self.output()
            print(f"{new_head_node.node_val} has been added")
        
        # Otherwise
        else:
            print("DLL is full!")

    def add_to_tail(self, new_node_value):
        new_tail_node = Node(new_node_value)
        old_tail_node = self.tail_node

        # If the size of the DLL hasn't reached the max size
        if self.size != self.max_size:
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

            # If there is no tail node and head node
            if self.tail_node == None and self.head_node == None:
                # Set the node passed into the function as the new tail node
                self.tail_node = new_tail_node
                # The new node will also be the new head node (if there was nothing before)
                self.head_node = new_tail_node

            # Increment the size of the DLL
            self.size += 1
            
            # Output the current state of the DLL
            self.output()
            print(f"{new_tail_node.node_val} has been added")
            return "successful"

        # Otherwise
        else:
            print("DLL is full!")
            return "unsuccessful"

    def remove_node(self, node_value_to_remove):
        start_current_node = self.head_node # Tracks the current node we are from the start of the list
        rear_current_node = self.tail_node # Tracks the current node we are from the end of the list
        node_to_remove = None # Will be set to the node to remove when found

        # FINDING THE NODE TO REMOVE
        
        # If the value of the current node at the start of the list is the same as the value of the node we want to remove
        if start_current_node.node_val[0] == node_value_to_remove:
            # Set the node to remove as the head node
            node_to_remove = self.head_node


        # If the value of the current node at the rear of the list is the same as the value of the node we want to remove
        if rear_current_node.node_val[0] == node_value_to_remove:
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
            if start_current_node.node_val[0] == node_value_to_remove:
                # Set the node to remove to be the current node
                node_to_remove = start_current_node

            # Check if the value of the rear current node is the same as the value of the node we want to remove
            if rear_current_node.node_val[0] == node_value_to_remove:
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

        # Return the node to remove (if it was None, None would have been returned already, so this addresses all other situations)
        return node_to_remove

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

    def find_node(self, node_value_to_find):
        start_current_node = self.head_node # Tracks the current node we are from the start of the list
        rear_current_node = self.tail_node # Tracks the current node we are from the end of the list
        node_to_find = None # Will be set to the current node to when found

        # If the value of the current node at the start of the list is the same as the value of the node we want to find
        if start_current_node.node_val[0] == node_value_to_find:
            # Set the node to remove as the head node
            node_to_find = self.head_node

        # If the value of the current node at the rear of the list is the same as the value of the node we want to find
        if rear_current_node.node_val[0] == node_value_to_find:
            # Set the node to  as the tail node
            node_to_find = self.tail_node

        # Move the current nodes inwards (As they cannot be the head node or tail node)
        start_current_node = start_current_node.next_node
        rear_current_node = rear_current_node.prev_node
        
        # While we haven't found the node
        while node_to_find == None:

            # If the rear current node has reached the start of the list and the start current node reached the end of the list
            if rear_current_node == self.head_node and start_current_node == self.tail_node:
                print("End of list reached, node not found!")
                break
            
            # Check if the value of the start current node is the same as the value of the node we want to find
            if start_current_node.node_val[0] == node_value_to_find:
                # Set the node to find to be the current node
                node_to_find = start_current_node

            # Check if the value of the rear current node is the same as the value of the node we want to find
            if rear_current_node.node_val[0] == node_value_to_find:
                # Set the node to find to be the current node
                node_to_find = rear_current_node

            # Increment the start current node (moves inwards towards the rear node)
            start_current_node = start_current_node.next_node
            # Decrement the start current node (moves inwards towards the head node)
            rear_current_node = rear_current_node.prev_node

        # ----------------------------------------------------------------------------------
        # RETURNING THE VALUES

        # In the case that the node was not found inside the DLL
        if node_to_find == None:
            # Return None
            return None
            
        # If the node has been found
        else: 
            # Return the node's value
            print(f"Found the node, returning value: {node_to_find.node_val[1]}")
            return node_to_find.node_val[1]

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

class HashMapDLL(HashMap):
    def __init__(self, array_size):
        super().__init__(array_size)

    def save(self, key, value):
        # Generate a hash code
        hash_code = self.hash(key)
        # Find an array index using the compressor
        array_index = self.compressor(hash_code)
        print(key, value, hash_code, array_index)

        # If the array in the arrays is empty
        if self.arrays[array_index] == None:
            # Save the key and value at the array at the index
            self.arrays[array_index] = [key, value]
            print(f"The value, {self.arrays[array_index][1]} has been saved to {array_index}.")

        # If the key in the array at the array index has the same key   
        elif self.arrays[array_index][0] == key:
            # Replace the value at the array index with the new value
            self.arrays[array_index][1] = value
            print(f"The new value, {self.arrays[array_index][1]} has been saved to {array_index}")

        # If the key in the array does not have the same key, but has been given the same array index
        elif self.arrays[array_index][0] != key:
            # If there isn't already a doubly linked list in the array at the array index
            if type(self.arrays[array_index][0]) != DoublyLinkedList:
                print("Not the same key, create a doubly linked list")
                # Create a doubly linked list
                array_dll = DoublyLinkedList(max_size = 2)
                # Set the head node as the existing key:value pair
                array_dll.add_to_head(self.arrays[array_index])
                # Add the current key:value pair to the end of the linked list
                array_dll.add_to_tail([key, value])
                # Replace the current key:value pair in the array at the index 
                self.arrays[array_index] = [array_dll]

            # If there is already a doubly linked list in the array at the array index
            else:
                print("first array index", array_index)
                # Add the current key:value pair to the end of the linked list
                return_value = self.arrays[array_index][0].add_to_tail([key,value])

                # In the case that the DLL at the array index was full, 
                if return_value == "unsuccessful":
                    # Add linear probing collision checking here
                    print("Look for another array index")

                    # Collision resolving
                    start_decrementing = False  
                    original_array_index = array_index

                    # While we haven't found an empty space
                    while True:
                        # CHECKING ITEM AT INDEX 
                        if self.arrays[array_index] == None:
                            # Save the key and value at the array at the index
                            self.arrays[array_index] = [key, value]
                            print(f"The value, {value} has been saved to {array_index}.")
                            break

                        # If the key in the array at the array index has the same key   
                        elif self.arrays[array_index][0] == key:
                            # Replace the value at the array index with the new value
                            self.arrays[array_index][1] = value
                            print(f"The new value, {value} has been saved to {array_index}")
                            break

                        # If the key in the array does not have the same key, but has been given the same array index
                        elif self.arrays[array_index][0] != key:
                            # If there isn't already a doubly linked list in the array at the array index
                            if type(self.arrays[array_index][0]) != DoublyLinkedList:
                                print("Not the same key, create a doubly linked list")
                                # Create a doubly linked list
                                array_dll = DoublyLinkedList(max_size = 2)
                                # Set the head node as the existing key:value pair
                                array_dll.add_to_head(self.arrays[array_index])
                                # Add the current key:value pair to the end of the linked list
                                array_dll.add_to_tail([key, value])
                                # Replace the current key:value pair in the array at the index 
                                self.arrays[array_index] = [array_dll]
                                break

                            # If there is already a doubly linked list in the array at the array index
                            else:
                                print("first array index", array_index)
                                # Add the current key:value pair to the end of the linked list
                                return_value = self.arrays[array_index][0].add_to_tail([key,value])


                        # INCREMENTING / DECREMENTING

                        # If the array index is the same as the array size, don't increment the array index
                        if array_index + 1 >= self.array_size:
                            # Start decrementing the array index
                            start_decrementing = True
                            # Set the array index to start from the item to the left of the item in the original array index
                            array_index = original_array_index - 1
                            continue
                        
                        # Otherwise
                        else:
                            # If we have reached the end of the hash map and have started decrementing
                            if start_decrementing == True:
                                # Decrement the array index
                                array_index -= 1

                                # If the array index goes below 0, it means we have searched the entire hash map without finding an empty space
                                if array_index < 0:
                                    print("No more space inside the hash map.")
                                    break
                            # If we haven't reached the end of the hash map
                            else:
                                # Increment the array index
                                array_index += 1

    def retrieve(self, key):
        # Generate a hash code
        hash_code = self.hash(key)
        # Find the array index using the compressor
        array_index = self.compressor(hash_code)

        print(key, hash_code, array_index)

        # If the array in the arrays is empty
        if self.arrays[array_index] == None:
            print("There is no value here.")

        # If the key in the array at the array index has the same key
        elif self.arrays[array_index] == key:
            print(f"Returning value: {self.arrays[array_index][1]}")
            return self.arrays[array_index][1]

        # If the key in the array does not have the same key, 
        elif self.arrays[array_index][0] != key:
            # If there is a doubly linked list at this array index
            if type(self.arrays[array_index][0]) == DoublyLinkedList:
                # Search the doubly linked list for the value
                return_value = self.arrays[array_index][0].find_node(key)

                # If the value returned was None, this means that it wasn't in this DLL. This could mean that the DLL was full and so the key:value pair was saved somewhere else.
                if return_value == None:
                    print("Not inside this DLL, so is somewhere else in the hash map.")

                    # COLLISION RESOLVING
                    
                    start_decrementing = False
                    original_array_index = array_index

                    # While we haven't found the item
                    while return_value == None:
                        # CHECKING ITEM AT INDEX
                        # If there is a doubly linked list at the current index 
                        if type(self.arrays[array_index][0]) == DoublyLinkedList:
                            # Search the doubly linked list for the value
                            return_value = self.arrays[array_index][0].find_node(key)   
                            
                            
                        # If there is no doubly linked list at the current index, it must mean that this is an array at this index
                        elif type(self.arrays[array_index]) == list:
                            # Return the value inside the array at the index
                            print(f"Returning value: {self.arrays[array_index][1]}")
                            return_value = self.arrays[array_index][1]
                            

                        # INCREMENTING / DECREMENTING
                        # If the array index is the same as the array size, don't increment the array index
                        if array_index + 1 == self.array_size:
                            # Start decrementing the array index
                            start_decrementing = True
                            # Set the array index to start from the item to the left of the item in the original array index
                            array_index = original_array_index - 1
                            continue
                        
                        # Otherwise
                        else:
                            # If we have reached the end of the hash map and have started decrementing
                            if start_decrementing == True:
                                # Decrement the array index
                                array_index -= 1

                                # If the array index goes below 0, it means we have searched the entire hash map without finding the item
                                if array_index < 0:
                                    print("Item not found.")
                                    break
                            # If we haven't reached the end of the hash map
                            else:
                                # Increment the array index
                                array_index += 1

                # If the value was correct i.e. not None.
                else:
                    return return_value

    def remove(self, key):
        # Generate a hash code
        hash_code = self.hash(key)
        # Find the array index using the compressor
        array_index = self.compressor(hash_code)

        print(key, hash_code, array_index)

        # If the array in the arrays is empty
        if self.arrays[array_index] == None:
            print("There is no value here.")

            # COLLISION RESOLVING
            
            start_decrementing = False
            original_array_index = array_index
            return_value = None

            # While we haven't found the item
            while return_value == None:
                # CHECKING ITEM AT INDEX

                # If the item at the index is None
                if self.arrays[array_index] == None:
                    print("There is no value here")

                # If there is a doubly linked list at the current index 
                elif type(self.arrays[array_index][0]) == DoublyLinkedList:
                    # Search the doubly linked list for the value
                    return_value = self.arrays[array_index][0].remove_node(key)  
                    # Convert the linked list back into an array if it only has one item
                    if self.arrays[array_index][0].head_node.node_val == self.arrays[array_index][0].tail_node.node_val:
                        # Set the item at the index to be an array again
                        self.arrays[array_index] = self.arrays[array_index][0].head_node.node_val
                        print("Linked list converted into array.")

                # If there is no doubly linked list at the current index, it must mean that this is an array at this index
                elif type(self.arrays[array_index]) == list and self.arrays[array_index][0] == key:
                    # Return the value inside the array at the index
                    print(f"Removing value: {self.arrays[array_index]}")
                    return_value = self.arrays[array_index][1]
                    # Remove the item at the index
                    self.arrays[array_index] = None
                    

                # INCREMENTING / DECREMENTING
                # If the array index is the same as the array size, don't increment the array index
                if array_index + 1 == self.array_size:
                    # Start decrementing the array index
                    start_decrementing = True
                    # Set the array index to start from the item to the left of the item in the original array index
                    array_index = original_array_index - 1
                    continue
                
                # Otherwise
                else:
                    # If we have reached the end of the hash map and have started decrementing
                    if start_decrementing == True:
                        # Decrement the array index
                        array_index -= 1

                        # If the array index goes below 0, it means we have searched the entire hash map without finding the item we want to remove
                        if array_index < 0:
                            print("Item not found.")
                            break
                    # If we haven't reached the end of the hash map
                    else:
                        # Increment the array index
                        array_index += 1

        # If the key in the array at the array index has the same key
        elif self.arrays[array_index][0] == key:
            #print(f"Removing item: {self.arrays[array_index][0]} : {self.arrays[array_index][1]}")
            print(f"Removed item: {self.arrays[array_index]}")
            # Set the array at the index to be None
            self.arrays[array_index] = None

        # If the key in the array does not have the same key, 
        elif self.arrays[array_index][0] != key or self.arrays[array_index] == None:
            # If there is a doubly linked list at this array index
            if type(self.arrays[array_index][0]) == DoublyLinkedList:
                # Search the doubly linked list for the value
                return_value = self.arrays[array_index][0].remove_node(key)

                # Convert the linked list back into an array if it only has one item
                if self.arrays[array_index][0].head_node.node_val == self.arrays[array_index][0].tail_node.node_val:
                    # Set the item at the index to be an array again
                    self.arrays[array_index] = self.arrays[array_index][0].head_node.node_val
                    print("Linked list converted into array.")

                # If the value returned was None, this means that it wasn't in this DLL. This could mean that the DLL was full and so the key:value pair was saved somewhere else.
                if return_value == None:
                    print("Not inside this DLL, so is somewhere else in the hash map.")

                    # COLLISION RESOLVING
                    
                    start_decrementing = False
                    original_array_index = array_index

                    # While we haven't found the item
                    while return_value == None:
                        # CHECKING ITEM AT INDEX

                        # If the item at the index is None
                        if self.arrays[array_index] == None:
                            print("There is no value here")

                        # If there is a doubly linked list at the current index 
                        elif type(self.arrays[array_index][0]) == DoublyLinkedList:
                            # Search the doubly linked list for the value
                            return_value = self.arrays[array_index][0].remove_node(key)  

                            # Convert the linked list back into an array if it only has one item
                            if self.arrays[array_index][0].head_node.node_val == self.arrays[array_index][0].tail_node.node_val:
                                # Set the item at the index to be an array again
                                self.arrays[array_index] = self.arrays[array_index][0].head_node.node_val
                                print("Linked list converted into array.")

                        # If there is no doubly linked list at the current index, it must mean that this is an array at this index
                        elif type(self.arrays[array_index]) == list and self.arrays[array_index][0] == key:
                            # Return the value inside the array at the index
                            print(f"Removing value: {self.arrays[array_index]}")
                            return_value = self.arrays[array_index][1]
                            # Remove the item at the index
                            self.arrays[array_index] = None
                            

                        # INCREMENTING / DECREMENTING
                        # If the array index is the same as the array size, don't increment the array index
                        if array_index + 1 == self.array_size:
                            # Start decrementing the array index
                            start_decrementing = True
                            # Set the array index to start from the item to the left of the item in the original array index
                            array_index = original_array_index - 1
                            continue
                        
                        # Otherwise
                        else:
                            # If we have reached the end of the hash map and have started decrementing
                            if start_decrementing == True:
                                # Decrement the array index
                                array_index -= 1

                                # If the array index goes below 0, it means we have searched the entire hash map without finding the item we want to remove
                                if array_index < 0:
                                    print("Item not found.")
                                    break
                            # If we haven't reached the end of the hash map
                            else:
                                # Increment the array index
                                array_index += 1

    def clear(self):
        # Replace the existing hash map with a new set of arrays
        self.arrays = [None for array in range(self.array_size)]

print("------------------------------------------------------------------------------------------------------------------------------------------------")
print("Doubly-linked list version")

my_hash_map_dll = HashMapDLL(10)
print(my_hash_map_dll.arrays)

# my_hash_map_dll.retrieve("Hello")
my_hash_map_dll.save("Hello", "World")
# my_hash_map_dll.save("Hello", "test")
my_hash_map_dll.save("Gsdau", "purple")
my_hash_map_dll.save("Adobe", "Company")
my_hash_map_dll.save("Zebra", "wheat")
my_hash_map_dll.save("Pet", "builder")
my_hash_map_dll.save("Rat", "plague")
my_hash_map_dll.save("Peter", "Amazing")
my_hash_map_dll.save("Girw", "Twenty")
my_hash_map_dll.save("nasa", "space")
my_hash_map_dll.save("bass", 3)
my_hash_map_dll.save("Circus", "clown")
my_hash_map_dll.save("Lionu", 97)
my_hash_map_dll.save("Zipz", 129)
# my_hash_map_dll.retrieve("Hello")
# my_hash_map_dll.retrieve("Bob")
# my_hash_map_dll.retrieve("Girw")
# my_hash_map_dll.retrieve("Ultra")
# my_hash_map_dll.retrieve("Zebra")
my_hash_map_dll.retrieve("Zipz")
my_hash_map_dll.retrieve("Circus")
print("---------------------------")
# # Testing all situations for removing items
# my_hash_map_dll.remove("Peter")
# my_hash_map_dll.remove("Lionu")
# my_hash_map_dll.remove("Girw")
# my_hash_map_dll.remove("Hello")
# my_hash_map_dll.remove("Adobe")
# my_hash_map_dll.remove("Gsdau")
# my_hash_map_dll.remove("Pet")
# my_hash_map_dll.remove("Zebra")
# my_hash_map_dll.remove("Rat")
# my_hash_map_dll.remove("bass")
# my_hash_map_dll.remove("Circus")
# my_hash_map_dll.remove("nasa")
# my_hash_map_dll.remove("Zipz")
# my_hash_map_dll.remove("sdasd") # Testing output if the key does not exist

print(my_hash_map_dll.arrays)
my_hash_map_dll.clear()
print(my_hash_map_dll.arrays)