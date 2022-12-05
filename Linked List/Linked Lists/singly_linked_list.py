class Node:
    def __init__(self, node_val, next_node = None):
        self.node_val = node_val
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head_node = Node(node_val = 50)
        
    def replace_head_node(self, new_node):
        # Set the new node to point at the head node
        new_node.next_node = self.head_node
        # Set the new node as the current new head node
        self.head_node = new_node

    
    def insert_new_node(self, new_node):
        # Set the current node as the head node
        current_node = self.head_node

        while True:
            # If the current node's next node is None, we have reached the end of the linked list
            if current_node.next_node == None:
                # Set the current item to point towards the new node
                current_node.next_node = new_node
                break
            # Go to the next node
            current_node = current_node.next_node

        print(f"{self.output()}, {new_node.node_val} has been added")


    def remove_node(self, value_to_remove):
        # Set the current node as the head node
        current_node = self.head_node

        while True:
            # If the head node is the value to remove
            if self.head_node.node_val == value_to_remove:
                self.head_node = self.head_node.next_node
                break

            else:
                # If the value of the node that the current node is pointing to is the same as the value to remove
                if current_node.next_node.node_val == value_to_remove:
                    # Set the current node's next node to be: the node that the node we want to remove is pointing to
                    current_node.next_node = current_node.next_node.next_node
                    break
                
                # Go to the next node
                current_node = current_node.next_node


    def output(self):
        # Set the current node as the head node
        current_node = self.head_node 
        list_of_items = []

        while True:
            # Append the current node's value to the list
            list_of_items.append(current_node.node_val)
            
            # Check if the current node's next node is None (meaning its the last item in the linked list)
            if current_node.next_node == None:
                # Leave the while loop
                break
            
            # Set the current node as the next node
            current_node = current_node.next_node

        return list_of_items



my_linked_list = LinkedList()

my_linked_list.replace_head_node(Node(20))
my_linked_list.replace_head_node(Node(2312))
print(my_linked_list.output())
print("----------------------------")

my_linked_list.insert_new_node(Node(5129392))

print("----------------------------")
my_linked_list.remove_node(50)
print(my_linked_list.output())