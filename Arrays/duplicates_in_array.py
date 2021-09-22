# Write a function that checks if a given array input has duplicates or not.
# [4, 3, 2, 7, 8, 2, 3, 1] -> True
# [4, 3, 2, 1] -> False

def duplicates_in_array(arr):
    '''
    This function checks if an array contains duplicates using hashmaps
    '''
    freq = {}

    for num in arr:
        # checks if num is repeated more than once in the array
        count = freq.get(num, 0) + 1
        if count > 1:
            return True

        freq[num] = count

    return False

# The above funcion can be simplified to this below
def duplicates_in_array_2(arr):
    '''
    This function checks if an array contains duplicates using hashmaps
    '''  
    for num in arr:
        if arr.count(num) > 1:
            return True
    return False



def duplicates_in_array3(arr):
    '''
    This fucntion checks if an array contains duplicates by comparing list with the outcome set
    '''
    return len(arr) == len(set(arr))


def duplicates_in_array_4(arr):
    '''
    This fucntion checks if an array contains duplicates by using sets
    '''
    # We can add num to the list and check if it is duplicated at the same time
    set_nums = set()

    for num in arr:
        if num in set_nums:
            return True
        else:
            set_nums.add(num)         
    return False