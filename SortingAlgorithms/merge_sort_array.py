def merge_sort(my_array):
    if len(my_array) > 1:
        # Check if length of array is greater than 1
        # Divide the the array into two and escape remainder
        mid_array = len(my_array) // 2
        left_side = my_array[:mid]
        right_side = my_array[mid:]

        # Recursive function on both halves
        mergeSort(left_side)
        mergeSort(right_side)

        # Two iterators for traversing the two halves and Iterator for the main array
        i, j, k = 0, 0, 0

        while i < len(left_side) and j < len(right_side):
            if left_side[i] < right_side[j]:
                # The value from the left_side half has been used
                my_array[k] = left_side[i]
                # Move the iterator forward
                i += 1
            else:
                my_array[k] = right_side[j]
                j += 1
            # Move to the next slot
            k += 1

        # For all the remaining values
        while i < len(left_side):
            my_array[k] = left_side[i]
            i += 1
            k += 1

        while j < len(right_side):
            my_array[k] = right_side[j]
            j += 1
            k += 1


'''
The algorithm works in O(n.logn).
This is because the list is being split in log(n) calls and the merging
process takes linear time in each call.

merge sort uses more space but less time 
'''

my_array = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(my_array)