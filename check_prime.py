import sys

def prime(enter, x):

    """ Calculates if the input is a prime number or not """

    if enter > 1 and x > 1:  # prime number must be greater than 1. BASE CASE

        result = enter % x   # enter / 1 but disregards the remainder

        if result != 0:  

            x = x-1          # checks n / every number below n until reach 0 
            prime(enter,x)   # recalls the function 

            return x

        elif result == 0:     

            print(str(enter) + " is not a prime number")

    else:                

        print(str(enter) + " is a prime number")
try:
    enter = 3
    x = enter - 1
    prime(enter,x)


except NameError:
    print("Input must be an integer")
    sys.exit()

except TypeError:        
    print("Input must be an integer")
    sys.exit()
