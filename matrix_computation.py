import sys

# Empty matrix to store answer

answer = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]] 

# Matricies to store resuts of calculations

calc_first_half = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
calc_second_half = [[0,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]


def matrix_addition(calc_first_half, B, C):

    """ Add all values in matrix B and C, store in calc_first_half """

    for i in range(len(B)):                # Adds each element in B with C

        for j in range(len(B[0])):

            calc_first_half[i][j] = B[i][j] + C[i][j]  # Stores result

    print("")
    print("B + C = ")
    print(calc_first_half)

    matrix_multiplication_second(calc_first_half,B,C)
    

def matrix_subtraction(answer, calc_first_half, calc_second_half):

    """ Subtracts all values in calc_first_half with calc_second_half """

    for i in range(len(B)):

        for j in range(len(B[0])):

            answer[i][j] = calc_first_half[i][j] - calc_second_half[i][j]
            
    # Stores result in "answer" which is the result of the given calculation
    

def matrix_multiplication(calc_second_half, B, C):

    """ Multiplies all B values with C values """

    for i in range(len(B)):     

        for j in range(len(B[0])):

            calc_second_half[i][j] = B[i][j] * C[i][j]

    print("")
    print("B * C = ")
    print(calc_second_half)
    

def matrix_multiplication_second(calc_first_half, B, C):

    """ Multiplies B + C by 2 """

    for i in range(len(B)):

        for j in range(len(B[0])):

            calc_first_half[i][j] = calc_first_half[i][j] * 2

    print("")
    print("2 * (B+C) = ")
    print(calc_first_half)


try:        # Catch Input Errors
    
            # Matricies for calculations

    B = [[1,2,3,4], [5,6,7,8], [9,10,1,2]],[3,4,5,6]]
    C = [[5,8,2,4], [6,1,8,2], [2,3,4,9], [10,7,9,5]]

    if len(B) == len(C):       # Length of matrices must be the same

        print("A = B*C - 2*(B+C) ")

        matrix_addition(calc_first_half, B, C)
        matrix_multiplication(calc_first_half, B, C)
        matrix_subtraction(answer, calc_first_half, calc_second_half)

        print("")
        print("Answer :")
        print(answer)

    else:
        print("The matricies must be the same size")

except NameError:
    
    print("Invalid Value in Matrix")
    sys.exit()
    
    
            

    
