import random
import sys

def random_shuffle(A,shuffled,length):

    """ Function to randomly shuffle an array of integers """

    a = random.choice(A)            # Random value from list A
    
    while length > 0:               # Base Case for recursion

        if a in shuffled:           # Cannot have duplicate values
            
            A.remove(a)           
            random_shuffle(A,shuffled,length)
            return shuffled
        
        else:
            
            shuffled.append(a)      # Add randomly chosen value 
            length = length-1       # Moves towards base case
            
            random_shuffle(A,shuffled,length)
            return shuffled

try:                                # Check for invalid input to avoid errors.
    
    A = ([1,3,4,6,7,2])             
    shuffled = []                   # New list to store randomly shuffled input
    length = len(A)

    random_shuffle(A,shuffled,length)

except NameError:
    
    print("Invalid input: Must be integers")
    sys.exit()
    
except IndexError:
    
    print("Invalid input: Must only be one of each number")
    sys.exit()


print(shuffled)
