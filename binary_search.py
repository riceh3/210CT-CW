def binary_search(entry):              # Divide and Conquer

    """ Search through input for values within the given high & low parameters """

    length = len(entry)
    middle = length/2
    middle = int(middle)

    if entry[middle] == low or entry[middle] == high:
        print("TRUE")

    elif middle < 1:        # Value not in range
        print("FALSE")

    else:

        if entry[middle] > low and entry[middle] < high:
            print("TRUE")

        elif low < entry[middle]:
            
            entry = entry[:middle]    # Disregard first half of list
            binary_search(entry)
            return entry

        elif high > entry[middle]:
            
            entry = entry[middle:]    # Disregard second half of list
            binary_search(entry)
            return entry
        
        else:
            print("FALSE")
try:
    
    entry = [2,3,5,7,9,13]
    low = 10
    high = 14

    if low < high:

        binary_search(entry)
        
    else:
        print("Low parameter must be less than High paramater")
        
except NameError:
    
    print("Input must be all integers")

