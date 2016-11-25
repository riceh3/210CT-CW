import sys

class Tree:

    """ Assigns values and left and right variables for tree structure """

    def __init__(self, value):             

        self.value = value
        self.right = None
        self.left = None

def insert_value(tree, item):             # Binary search tree
    
    """ Insert values into Binary Tree structure """

    if tree == None:
        tree = Tree(item)                 # Makes values NONE

    else:

        if (item < tree.value):           # Left side must be smaller
            
            if (tree.left == None):
                tree.left = Tree(item)    # Becomes the new root

            else:
                insert_value(tree.left,item)   

        else:                             # Right side must be larger

            if(tree.right == None):
                tree.right = Tree(item)

            else:
                insert_value(tree.right, item)   

    return tree      

def in_order_iterative(tree_root):

    """ Orders Nodes in Left, Node, Right (in order) structure """

    current = tree_root                   # Root of tree(top value in tree)

    stack = []                            # LIFO (last in first out)

    while True:

        while current != None:            # A leaf has no children

            stack.append(current)         # Add values into stack
            current = current.left        # Continue moving left

        if current == None:               # No more children

            length = len(stack)

            # Stack will only be empty once all nodes have been added to order

            if length > 0:
                
                current = stack.pop()     # Takes last in stack value
                
                                          # Value gets removed from stack at the same time
                
                print(current.value)
                current = current.right   # Now we have gone left, need to go right

            else:
                sys.exit()                # Stop infinite loop

                
                                          # Example Graph for Visual representation 
                
t = insert_value(None,10)                 #                 10
tree_root = insert_value(None, None)      #               /    \ 
tree_root.left = insert_value(t, 8)       #              8      14
insert_value(t, 14)                       #             / \    /  \
insert_value(t, 5)                        #            5   9  12  17 
insert_value(t, 9)                        #                  /  \ 
insert_value(t, 12)                       #                 11   13 
insert_value(t, 17)
insert_value(t, 11)
insert_value(t, 13)

in_order_iterative(tree_root)  



