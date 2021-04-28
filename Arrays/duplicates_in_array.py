# Write a function that checks if a given array input has duplicates or not.
# [4, 3, 2, 7, 8, 2, 3, 1] -> True
# [4, 3, 2, 1] -> False

def duplicates_in_array(arr):
    '''
    This fucntion checks if an array contains duplicates using hashmaps
    '''
    freq = {}

    for num in arr:
        # checks if num is repeated more than once in the array
        count = freq.get(num, 0) + 1

        if count > 1:
            return True

        freq[num] = count

    return False
