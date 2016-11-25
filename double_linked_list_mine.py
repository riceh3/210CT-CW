class Node:

    """ Establishes Node with connected Nodes """

    def __init__(self, value):

        self.value = value
        self.next = None
        self.prev = None

class Double_Linked_List:
    
    """ Insert given nodes and remove given nodes to and from a double linked list """

    def __init__(self):

        self.head = None
        self.tail = None

    def insert_node(self, node, point):

        """ Insert given node into the linked list """

        if node != None:                

            point.next = node.next             # Point next node
            node.next = point                  # New next node is point
            point.prev = node                  # Point to previous node

            if point.next != None:
                point.next.prev = point

        if self.head == None:                  # When list is empty 
            
            self.head = self.tail = point      # Head and tail will equal the node
            point.prev = point.next = None     # Nothing to point to because list was empty

        elif self.tail == node:
            self.tail = point       
# ------------------------------------------------------------------- |
    def remove_node(self, node):

        """ Remove given node from the linked list """

        if node.prev != None:                  # Previous node will point to next node
            node.prev.next = node.next

        else:                                  
            self.head = node.next

        if node.next != None:                  # Next node now equals the previous
            node.next.prev = node.prev

        else:
            self.tail = node.prev
# ------------------------------------------------------------------- |
    def show_list(self):

        """ Displays the linked list """

        values = []                            # Creates the list type
        node = self.head

        while node != None:

            values.append(str(node.value))     # Adds nodes to list 

            node = node.next

        print(" ---> ".join(values))           # .join = returns string, elements joined by str operation

if __name__ == '__main__':

    l = Double_Linked_List()
    l.insert_node(None, Node(4))
    l.insert_node(l.head, Node(6))
    l.insert_node(l.head, Node(8))
    l.insert_node(l.head, Node(3))
    l.insert_node(l.head, Node(2))
    l.show_list()
    l.remove_node(l.head)
    l.show_list()

    
