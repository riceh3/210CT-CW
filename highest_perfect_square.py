import sys
def highest_perfect_square(enter):

    """ Returns the highest perfect square which is less than or equal to input """

    factor = 0

    if enter >= 0:          

        while factor*factor < enter:      

            factor = factor + 1     # 1*1, 2*2, 3*3, etc

        if factor*factor == enter:      # Either the first input or less than n
            
            print(str(enter) + " is a perfect square number")

        else:
            enter = enter-1           # counts down from n, until perfect square
            
            highest_perfect_square(enter)

    else:
        
        print("invalid input")
            
try:
    enter = (36)
    highest_perfect_square(enter)

except NameError:
    print("Invalid Input")
    sys.exit()
    
except TypeError:
    print("Invalid Input")
    sys.exit()
