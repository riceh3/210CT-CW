import sys

def reverse_sentence(s):

    """ Takes 's' as input then reverses the string """

    sLength = len(s)

    if sLength <= 0:        # Stops infinite recursion
                            # The function stops once the sentence in reversed

        return s

    else:

        sLength = sLength-1   
        
        s = s
        reverse_sentence(s[1:]) + s[0:]   # Recalls the function with new '0'
        
        position = s[0]                   # Saves position 0 value
                                          # S[0] changes each itteration
        print(position)   
        return  s                         # Continues through the input


sentence = ("This is awesome")            # Original input

if type(sentence) != str:                 # Catch for input errors
    
    print("Input must be a string")
    sys.exit()

s = sentence.split()        # Split so that can index each word in sentence

print(sentence)
print("")
print("REVERSED: ")
print("")

reverse_sentence(s)
