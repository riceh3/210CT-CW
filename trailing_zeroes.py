import sys
def factorial_trailing_zeroes(n):

    """ Function first detemines the factorial of input """
    """ Then calculates the number of trailing zeroes """

    if n > 0:    # A factorial number must be greater than 0

        factorial = 1

        for i in range(1, n+1): # Loop range detemined by input

           factorial = (factorial*i)  # Determines the factorial of input

           # (1*1 = 1), (1*2 = 2), (2*3 = 6), (6*4 = 24), etc...

           calc = (5**(i-1)) # Determines trailing zeroes
           # eg: (5**0, 5**1, 5**2, 5**3, 5**4)
           print(calc)
           calc = int(calc)
           ans = (factorial/calc)

           
           ans = int(ans)
           trailing_zeroes = (ans + 1)


        print(str(n) + "!" + " = " + str(factorial))
        print("The number of trailing zeroes are " + str(trailing_zeroes))
        

    else:

        print("Input must be greater than zero")

try:
    n = (5)
    factorial_trailing_zeroes(n)

# Expect potential false input
    
except NameError:
    print("Invalid Input: Must be a whole number")
    sys.exit()
except TypeError:
    print("Invalid Input: Must be an integer")
    sys.exit()
