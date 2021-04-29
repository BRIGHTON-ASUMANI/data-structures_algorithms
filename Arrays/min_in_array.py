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


def min_array3(arr):
    '''
    This fucntion returns the minimum number in a number assuming the first number is the smallest
    '''
    first_element = arr[0]  # Start by assuming the first element is smallest
    for num in arr:       # Loop through each number in the list
        if num < first_element:
            first_element = num  # Update first_element if current number is less
    return first_element
