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

        # If the array in the arrays is empty
        if self.arrays[array_index] == None:
            print("None")
            # Save the key and value at the array at the index
            self.arrays[array_index] = [key, value]
        # If the key in the array at the array index has the same key
        elif self.arrays[array_index][0] == key:
            print("The same")

        # If the key in the array does not have the same key, 
        elif self.arrays[array_index][0] != key:
            print("Not the same key, go to another index")
            # Add collision handling

    def retrieve(self, key):
        # Generate a hash code
        hash_code = self.hash(key)
        # Find the array index using the compressor
        array_index = self.compressor(hash_code)

        # If the array in the arrays is empty
        if self.arrays[array_index] == None:
            print("Nothing here")

        # If the key in the array at the array index has the same key
        elif self.arrays[array_index][0] == key:
            print("Returning value", self.arrays[array_index][1])
            return self.arrays[array_index][1]

        # If the key in the array does not have the same key, 
        elif self.arrays[array_index][0] != key:
            print("Not the same key, go to another index")
            # Add collision handling 


my_hash_map = HashMap(10)   
my_hash_map.save("Hello", "World")
my_hash_map.save("Hello", "test")
my_hash_map.save("Goodk", "sd")
my_hash_map.save("Lyle", "Programmer")
my_hash_map.retrieve("Hello")
my_hash_map.retrieve("Lyle")