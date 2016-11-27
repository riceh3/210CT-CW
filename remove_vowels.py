import sys

def remove_vowels(word, vowels, position, word_copy):

    """ Takes input and returns the input without the vowels """

    if position > 0:                                 # Base case
        
        # Itterates through vowels, also moves towards base case
        
        position = position-1  

        if vowels[position] in word:

            # Each call checks if that vowel is in the input
            
            a = vowels[position]
            
            word_copy = word_copy.replace(a,"")      # Takes out the vowel
            print(word_copy)
            

            remove_vowels(word,vowels,position,word_copy) 
            return position
            

        else:                                        # Moves to next vowel
            
            remove_vowels(word,vowels,position,word_copy)  
            return position
    else:
        
        return position


word = ("beautiful")

if type(word) != str:                                # Check for input errors
     
    print("Input must be a string")
    sys.exit()
    
vowels = ("a","e","i","o","u","A","E","I","O","U")
position = len(vowels)
word_copy = word

print(word)         # If there are no vowels the input word will show

remove_vowels(word,vowels,position,word_copy)
