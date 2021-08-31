'''
There are four types of steps that occur in Insertion Sort: removals,
comparisons, shifts, and insertions. To analyze the efficiency of Insertion
Sort, we need to tally up each of these steps.

Big O = O((N*N) + 2N - 2) = O(N*N + N) = O(N*N) 
'''


def insertion_sort(array):

    for index in range(1, len(array)):
        '''
        First, we start a loop beginning at index 1 that runs through the entire array.
        The current index is kept in the variable index .
        '''
        position = index
        temp_value = array[index]
        '''
        Next, we mark a position at whatever index currently is. We also assign the
        value at that index to the variable temp_value .
        '''
        while position > 0 and array[position - 1] > temp_value:
            '''
            We then begin an inner while loop. We check whether the value to the left of
            position is greater than the temp_value . If it is, we then use array[position] =
            array[position - 1] to shift that left value one cell to the right, and then
            decrement position by one. We then check whether the value to the left ofthe new position is greater than temp_value , and keep repeating this process
            until we find a value that is less than the temp_value .
            '''
            array[position] = array[position - 1]
            position = position - 1
        '''
        Finally, we drop the temp_value into the gap within the array.
        '''
        array[position] = temp_value


# Python program for implementation of Insertion Sort

# Function to do insertion sort
def insertionSort2(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])

# This code is contributed by Mohit Kumra
