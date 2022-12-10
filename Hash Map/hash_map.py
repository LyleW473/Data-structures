class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.arrays = [None for array in range(array_size)] # Create arrays with the value None, array_size times

    def hash(self, key):
        # Encode the key, add the sum of all the numbers and that will be the hash code. Return the hash code.
        return sum(key.encode())

    def compressor(self, hash_code):
        # Return hash_code MOD array size. This is so that the array index that is returned will always be within the boundaries of the array.
        return hash_code % self.array_size
    
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
            print(f"Value, {self.arrays[array_index][1]} has been saved to {array_index}.")

        # If the key in the array at the array index has the same key
        elif self.arrays[array_index][0] == key:
            # Replace the value at the array index with the new value
            self.arrays[array_index][1] = value
            print(f"The new value, {self.arrays[array_index][1]} has been saved to {array_index}")

        # If the key in the array does not have the same key, 
        elif self.arrays[array_index][0] != key:
            print("Not the same key, go to another index")
            
            # Collision handling    
            start_decrementing = False
            original_array_index = array_index # Saves the original array index so that if we check all the spaces to the right of the original array index, we want to go to the left starting from the original spot again

            # While the array at the index is not empty
            while self.arrays[array_index][0] != None:
                print(f"Array index = {array_index}")

                # Check if we have reached the final index of the array without finding an empty spot and have started decrementing
                if start_decrementing == True:  

                    # If array_index is less than 0, it means that we have checked all indexes to the left and right of the original array index.
                    if array_index < 0:
                        print("There is no more space in the array.")
                        break

                    # If the array index isn't less than 0
                    else:
                        # Decrement the array index
                        array_index -= 1  
        
                        # If the array at the index is empty
                        if self.arrays[array_index] == None:
                            # Save the key and value to the array at the index
                            print("old", self.arrays[array_index], "at", array_index)
                            self.arrays[array_index] = [key, value]
                            print("new", self.arrays[array_index], "at", array_index)
                            break

                        # If the key in the array at the array index has the same key
                        elif self.arrays[array_index][0] == key:
                            # Replace the value at the array index with the new value
                            self.arrays[array_index][1] = value
                            print(f"The new value, {self.arrays[array_index][1]} has been saved to {array_index}")
                            break


                # If the array index + 1 is less than the array size (maximum index would be the array_size - 1) and we aren't decrementing yet
                # Note: It is array_index + 1 because if the max size was 5, we would want to check if array_index + 1 < 5 before incrementing array_index.
                if array_index + 1 < self.array_size and start_decrementing == False:
                    # Increment the array index
                    array_index += 1

                    # If the array at the index is empty
                    if self.arrays[array_index] == None:
                        # print("Entered")
                        # print("Save value and key")
                        print("old", self.arrays[array_index])
                        # Save the key and value to the array at the index
                        self.arrays[array_index] = [key, value]
                        print("new", self.arrays[array_index])
                        break

                    # If the key in the array at the array index has the same key
                    elif self.arrays[array_index][0] == key:
                        # Replace the value at the array index with the new value
                        self.arrays[array_index][1] = value
                        print(f"The new value, {self.arrays[array_index][1]} has been saved to {array_index}")
                        break

                # If we have reached the end of the array
                elif array_index + 1 >= self.array_size:
                    print("Cannot go this way anymore, start decrementing.")
                    start_decrementing = True           
                    # Set the array index to start from the left item of the original index again, this is so that we don't start decrementing from the end of the array. 
                    # Note: The possibility that there is a space at original_array_index has been eliminated, so start from the item to the left of the original index.
                    array_index = original_array_index - 1
                    continue
                
            # Print all the arrays in the hash map
            print(self.arrays)

    def retrieve(self, key):
        # Generate a hash code
        hash_code = self.hash(key)
        # Find the array index using the compressor
        array_index = self.compressor(hash_code)

        # If the array in the arrays is empty
        if self.arrays[array_index] == None:
            print("There is no value here.")

        # If the key in the array at the array index has the same key
        elif self.arrays[array_index][0] == key:
            print(f"Returning value: {self.arrays[array_index][1]}")
            return self.arrays[array_index][1]

        # If the key in the array does not have the same key, 
        elif self.arrays[array_index][0] != key:
            print("Not the same key, go to another index")
        
            # Collision handling    
            start_decrementing = False
            original_array_index = array_index # Saves the original array index so that if we check all the spaces to the right of the original array index, we want to go to the left starting from the original spot again
            # While the array at the index is not the key
            while self.arrays[array_index][0] != key:
                print(f"Array index = {array_index}")

                # Check if we have reached the final index of the array without finding an empty spot and have started decrementing
                if start_decrementing == True:  

                    # If array_index is less than 0, it means that we have checked all indexes to the left and right of the original array index.
                    if array_index < 0:
                        print("This item you are looking for is not in the hash map.")
                        break

                    # If the array index isn't less than 0
                    else:
                        # Decrement the array index
                        array_index -= 1  

                        # If the key in the array at the array index is the same as the key passed in
                        if self.arrays[array_index][0] == key:
                            # Return the value in that array
                            print(f"Returning value: {self.arrays[array_index][1]}")
                            return self.arrays[array_index][1]

                # If the array index + 1 is less than the array size (maximum index would be the array_size - 1) and we aren't decrementing yet
                # Note: It is array_index + 1 because if the max size was 5, we would want to check if array_index + 1 < 5 before incrementing array_index.
                if array_index + 1 < self.array_size and start_decrementing == False:
                    # Increment the array index
                    array_index += 1

                    # If the key in the array at the array index is the same as the key passed in
                    if self.arrays[array_index][0] == key:
                        # Return the value in that array
                        print(f"Returning value: {self.arrays[array_index][1]}")
                        return self.arrays[array_index][1]
                    
                # If we have reached the end of the array
                elif array_index + 1 >= self.array_size:
                    print("Cannot go this way anymore, start decrementing.")
                    start_decrementing = True           
                    # Set the array index to start from the left item of the original index again, this is so that we don't start decrementing from the end of the array. 
                    # Note: The possibility that there is a space at original_array_index has been eliminated, so start from the item to the left of the original index.
                    array_index = original_array_index - 1
                    continue

    def remove(self, key):
        # Generate a hash code
        hash_code = self.hash(key)
        # Find the array index using the compressor
        array_index = self.compressor(hash_code)

        # If the array in the arrays is empty
        if self.arrays[array_index] == None:
            print("There is no value here.")

            # Collision handling    
            start_decrementing = False
            original_array_index = array_index # Saves the original array index so that if we check all the spaces to the right of the original array index, we want to go to the left starting from the original spot again

            # While we haven't found the item we want to remove
            while self.arrays[array_index] != key:
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

                # CHECKING ITEM AT INDEX

                if self.arrays[array_index] == None: 
                    print("There is no value here")
                    pass

                # If the key in the array at the array index has the same key   
                elif self.arrays[array_index][0] == key:
                    # Set the array at the index to be None (REMOVE THE ITEM)
                    print(f"Item found at array index: {array_index}\n{self.arrays[array_index]} has been removed.")
                    self.arrays[array_index] = None
                    # Output the hash map
                    print(self.arrays)

                    break

        # If the key in the array at the array index has the same key   
        elif self.arrays[array_index][0] == key:
            # Set the array at the index to be None (REMOVE THE ITEM)
            print(f"Item found at array index: {array_index}\n{self.arrays[array_index]} has been removed.")
            self.arrays[array_index] = None
            # Output the hash map
            print(self.arrays)

        # If the key in the array does not have the same key, 
        elif self.arrays[array_index][0] != key:
            print("Not the same key, go to another index")

            # Collision handling    
            start_decrementing = False
            original_array_index = array_index # Saves the original array index so that if we check all the spaces to the right of the original array index, we want to go to the left starting from the original spot again
            
            # While we haven't found the item we want to remove
            while self.arrays[array_index] != key:
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

                # CHECKING ITEM AT INDEX

                # If the key in the array at the array index has the same key   
                if self.arrays[array_index][0] == key:
                    # Set the array at the index to be None (REMOVE THE ITEM)
                    print(f"Item found at array index: {array_index}\n{self.arrays[array_index]} has been removed.")
                    self.arrays[array_index] = None
                    # Output the hash map
                    print(self.arrays)

                    break

                
 
my_hash_map = HashMap(5)   
my_hash_map.retrieve("Hello")
my_hash_map.save("Hello", "World")
my_hash_map.save("Hello", "test")
print("------------------------------")
my_hash_map.save("Goodk", "sd")
my_hash_map.save("Lyle", "Programmer")
my_hash_map.save("Rice", "three")
my_hash_map.save("Bread", "food")
my_hash_map.save("Noodles", "soup")
my_hash_map.save("Bond", "blue")
my_hash_map.save("Rice", "five")
my_hash_map.save("French fries", "restaurant")

print("------------------------------")
# my_hash_map.retrieve("Hello")
# my_hash_map.retrieve("Lyle")
# my_hash_map.retrieve("Noodles")
#my_hash_map.retrieve("Puppy")

my_hash_map.remove("Lyle")
my_hash_map.remove("Hello")
my_hash_map.remove("Rice")
my_hash_map.remove("Bread")
my_hash_map.remove("Goodk")
my_hash_map.remove("dsakd")