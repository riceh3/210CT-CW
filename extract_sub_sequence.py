import sys
class Extract_Sub_Sequence:

    """ Extract the sub sequence of maximum length in ascending order """

    def __init__(self, sequence):

        self.sequence = sequence
        Extract_Sub_Sequence.search_sequence(self)

    def search_sequence(self):

        point = (self.sequence[0])  

        start = sequence[0]    # Start search at first element
        
        A = [start]
        B = []                 # Will store new sub sequences for length comparison
        
        for i in range(len(sequence)):

            if self.sequence[i] > self.sequence[i-1]:   # Ascending order
                
                point = self.sequence[i]
                A.append(point)             # Store sub sequence value
                print(A)
                
            else:
                
                if len(A) > len(B):            # Puts current value into new A[]   
                    B = A

                A = [sequence[i]]
                    
        if len(A) > len(B):
            print("")
            print(A)
        else:
            print("")
            print(B)
                    
        
              
sequence = [1,2,3,4,1,5,1,6,7]

Extract_Sub_Sequence(sequence)

