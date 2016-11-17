import random
import sys

def random_shuffle(A,shuffled,length):

    """ Function to randomly shuffle an array of integers """

    a = random.choice(A)
    
    while length > 0:               # Base Case for recursion

        if a in shuffled:
            A.remove(a)           
            random_shuffle(A,shuffled,length)
            return shuffled
        
        else:
            shuffled.append(a)
            length = length-1
            random_shuffle(A,shuffled,length)
            return shuffled

try:                                # Check for invalid input to avoid errors.
    
    A = ([1,3,4,6,7,2])             # Input
    shuffled = []
    length = len(A)

    random_shuffle(A,shuffled,length)

except NameError:
    
    print("Invalid input: Must be integers")
    sys.exit()
    
except IndexError:
    print("Invalid input: Must only be one of each number")
    sys.exit()


print(shuffled)
