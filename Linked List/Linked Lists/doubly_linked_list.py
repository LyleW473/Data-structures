class Node:
    def __init__(self, node_val, next_node = None, prev_node = None):
        self.node_val = node_val
        self.next_node = next_node
        self.prev_node = prev_node

class DoublyLinkedList:
    def __init__(self):
        self.head_node = None
        self.tail_node = None

    def add_to_head(self, new_head_node):
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
        
    def output(self):
        current_node = self.head_node # Node used to iterate through the LL
        list_of_items = [] # List to hold the values of all the nodes in the LL

        while current_node != None:
            # Append the value of the current node
            list_of_items.append(current_node.node_val)
            # Go to the next node
            current_node = current_node.next_node

        print(list_of_items)


my_dll = DoublyLinkedList()
my_dll.add_to_head(Node(97))
my_dll.add_to_head(Node(58))
my_dll.add_to_head(Node(32))
my_dll.add_to_head(Node(100))
my_dll.add_to_head(Node(23))
my_dll.output()

