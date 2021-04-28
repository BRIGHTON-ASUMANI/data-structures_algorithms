# Write a function that returns the minimun number in an array.
# [4, 3, 2, 1, 7, 8, 2, 3] -> 1
# [4, 3, 2, -21] -> -21
def min_array(arr):
    '''
    This fucntion returns the minimum number in a given array using min
    '''
    return min(arr)


def min_array2(arr):
    '''
    This fucntion returns the minimum number in a given array using sorted
    '''
    return sorted(arr)[0]
