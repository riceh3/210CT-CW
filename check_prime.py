import sys

def prime(enter, x):

    """ Calculates if the input is a prime number or not """

    if enter > 1 and x > 1:   # Prime number must be greater than 1

        result = enter % x    # Enter / 1 but disregards the remainder

        if result != 0:  

            x = x-1           # Checks n / every number below n until reach 0 
            prime(enter,x)   

            return x

        elif result == 0:     

            print(str(enter) + " is not a prime number")

    else:                

        print(str(enter) + " is a prime number")
        
try:                          # Catch for input errors
    
    enter = 3
    
    if enter > 1:
        x = enter - 1
        prime(enter,x)
        
    else:
        print("Input must be greater than 1")


except NameError:
    
    print("Input must be an integer")
    sys.exit()

except TypeError:
    
    print("Input must be an integer")
    sys.exit()
