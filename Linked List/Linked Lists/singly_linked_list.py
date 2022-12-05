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
        # Set the searching node to be the node after the head node (as this would only be accessed if it was proven that node1 / node2 is not the head node)
        other_node = self.head_node.next_node

        # Check if the values are the same before starting the swapping process
        if node1_value == node2_value:  
            print("These values are the same.")
            # Exit the function
            return

        # Search for node1 and node1prev
        while True:
            # If the head node's value is the same as the node 1 value
            if self.head_node.node_val == node1_value:
                # Set node 1 to be the same as the head node
                node1 = self.head_node
                # This node does not have a previous node
                node1_prev = None
                break

            else:
                # If value of the node after the head node is the same as node 1
                if other_node.node_val == node1_value:
                    # Set node 1 as the node after the head node
                    node1 = other_node
                    node1_prev = self.head_node
                    break
                # Otherwise
                else:
                    # Set the previous node as the current node
                    node1_prev = other_node
                    # Set the current node to be the next node
                    other_node = other_node.next_node

        # Search for node2 and node2prev
        while True:
            # If the head node's value is the same as the node 1 value
            if self.head_node.node_val == node2_value:
                # Set node 2 to be the same as the head node
                node2 = self.head_node
                # This node does not have a previous node
                node2_prev = None
                break
            else:
                # If value of the node after the head node is the same as node2
                if other_node.node_val == node2_value:
                    # Set node 2 as the node after the head node
                    node2 = other_node
                    node2_prev = self.head_node
                    break
                # Otherwise
                else:
                    # Set the previous node as the current node
                    node2_prev = other_node
                    # Set the current node to be the next node
                    other_node = other_node.next_node


        # SWAPPING THE FIRST TWO ITEMS

        # If node 1 is the first item (This means that node 1 is the head node)
        if node1_prev == None:
            # Set the head node as node1
            self.head_node = node1


            # Set node 1 point to the node that node 2 is pointing to. Set node 2 point towards node 1
            node1.next_node, node2.next_node = node2.next_node, node1

            # Set node 2's previous node to be node 1's previous node (this is None). Set node 1's previous node to be node 2 
            node2_prev, node1_prev = node1_prev, node2

            # Set the head node to be node 2 
            self.head_node = node2
        
        # If node 2 is the first item (This means that node 2 is the head node)
        elif node2_prev == None:
            # Set the head node as node2
            self.head_node = node2
            
            # Set node 1 point to the node that node 2 is pointing to. Set node 2 point towards node 1
            node2.next_node, node1.next_node = node1.next_node, node2

            # Set node 2's previous node to be node 1's previous node (this is None). Set node 1's previous node to be node 2 
            node1_prev, node2_prev = node2_prev, node1

            # Set the head node to be node 2 
            self.head_node = node1

        
        # SWAPPING ANY ITEMS
        # - Add here



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

new_linked_list.swap_nodes(0, 50)

print(new_linked_list.output())

