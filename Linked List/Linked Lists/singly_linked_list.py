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

    def swap_nodes(self, node1_value, node2_value):

        # If the nodes are the same, then just exit the function
        if node1_value == node2_value:  
            print("These values are the same.")
            # Exit the function
            return

        # Search for node 1 and the node previous to it
        prev_node_1 = None
        current_node = self.head_node
        while True:
            # If the current node's value is the same as the node 1 value
            if current_node.node_val == node1_value:
                # Set node 1 as this node
                node1 = current_node
                break
            
            # Set the previous node as the current node
            prev_node_1 = current_node
            # Go to the next node
            current_node = current_node.next_node


        # Do the same for node 2
        prev_node_2 = None
        current_node = self.head_node

        while True:
            # If the current node's value is the same as the node 2 value
            if current_node.node_val == node2_value:
                # Set node 2 as this node
                node2 = current_node
                break
            
            # Set the previous node as the current node
            prev_node_2 = current_node
            # Go to the next node
            current_node = current_node.next_node

        # Swapping:

        # If node 1 is the head node
        if prev_node_1 == None:

            # Set the previous node 1 to remain the same. Set previous node 2 to point to node 1
            prev_node_2.next_node = node1   # Same as: prev_node_1, prev_node_2.next_node = None, node1

            # Check if the element they want to swap is the first and last item:
            if node2.next_node == None: 
                # Set node 2's previous node to be node 1
                prev_node_2.next_node = node1
                # Set node 1's next node to be nothing (last item points to nothing), and set node 2's next node to be node 1
                node1.next_node, node2.next_node = None, node1.next_node

            # If it isn't, they are swapping the first item with any other item
            else:
                # Swap the next node pointers of node 1 and node 2
                node2.next_node, node1.next_node = node1.next_node, node2.next_node

            # Set the head node as the node 2 
            self.head_node = node2

        # If node 2 is the head node
        elif prev_node_2 == None:
        
            # Set the previous node 2 to remain the same. Set previous node 1 to point to node 2
            prev_node_1.next_node = node2   # Same as: prev_node_2, prev_node_1.next_node = None, node2

            # Check if the element they want to swap is the first and last item:
            if node1.next_node == None: 
                # Set node 1's previous node to be node 2
                prev_node_1.next_node = node2
                # Set node 2's next node to be nothing (last item points to nothing), and set node 1's next node to be node 2
                node2.next_node, node1.next_node = None, node2.next_node

            # If it isn't, they are swapping the first item with any other item
            else:
                # Swap the next node pointers of node 1 and node 2
                node1.next_node, node2.next_node = node2.next_node, node1.next_node

            # Set the head node as the node 2 
            self.head_node = node1


        # Swapping between elements other than the first 
        else:
            # Swap the next node pointers of the previous nodes
            prev_node_1.next_node, prev_node_2.next_node = prev_node_2.next_node, prev_node_1.next_node 
            # Swap the next node pointers of node 1 and node 2
            node1.next_node, node2.next_node = node2.next_node, node1.next_node
    


my_linked_list = LinkedList()

my_linked_list.replace_head_node(Node(20))
my_linked_list.replace_head_node(Node(2312))
print(my_linked_list.output())
print("----------------------------")

my_linked_list.insert_new_node(Node(5129392))

print("----------------------------")
my_linked_list.remove_node(50)
print(my_linked_list.output())

print("-----------------------------------------------------------------------------------------------------")
new_linked_list = LinkedList()
for i in range(10):
    new_linked_list.insert_new_node(Node(i))

new_linked_list.swap_nodes(2, 50)
print(new_linked_list.output())

