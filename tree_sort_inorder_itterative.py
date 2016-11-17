class Tree:

    def __init__(self, value):             # clears tree to start

        self.value = value
        self.right = None
        self.left = None

def insert_value(tree, item):   # Binary search tree
    
    """ Insert values into Binary Tree structure """

    if tree == None:
        tree = Tree(item)        # makes values NONE

    else:

        if (item < tree.value):   # left side must be smaller
            
            if (tree.left == None):
                tree.left = Tree(item) # becomes the new root

            else:
                insert_value(tree.left,item)   # recalls 

        else:                          # right side must be larger

            if(tree.right == None):
                tree.right = Tree(item)

            else:
                insert_value(tree.right, item)   # recalls

    return tree       # RECURSIVE

def in_order_iterative(tree_root):

    """ Traverse tree in order (Left,Node,Right) """

    current = tree_root       # Root of tree (top value)

    stack = []           # Create stack
    stop = 0

    while True:

        if current != None:           # Leaf = no children

            stack.append(current)     # Add value to stack = first in order
            current = current.left    # Move to next left value

        else:

            length = len(stack)       # If current has a value then it will have been added to stack 

            if length > 0:

                current = stack.pop()   # List method - will remove top element from stack

                print(current.value)
                current = current.right  # Move to previous then check if points right

            else:

                stop = 1              # Stops infinite loop, while = False


# DOESN'T MATTER WHAT ORDER WE ENTER IT WILL BE SORTED INTO BINARY TREE

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



