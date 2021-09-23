def binary_search(arr, value):
    # First, we establish the lower and upper bounds of where the value
    # we're searching for can be. To start, the lower bound is the first
    # value in the array, while the upper bound is the last value:
    lower_bound, upper_bound, mid = 0, len(arr) - 1, 0

    # We begin a loop in which we keep inspecting the middlemost value
    # between the upper and lower bounds:
    while lower_bound <= upper_bound:
        mid = (upper_bound + lower_bound) // 2

        # If value is greater, ignore left half
        if arr[mid] < value:
            lower_bound = mid + 1

        # If value is smaller, ignore right half
        elif arr[mid] > value:
            upper_bound = mid - 1

        # means value is present at mid
        else:
            return mid

    # If we reach here, then the element was not present
    return -1


# This is binary search using recursive functions
# Returns index of x in arr if present, else -1
def binary_search_2(arr, low, high, x):

    # Check base case
    if high >= low:

        mid = (high + low) // 2

        # If element is present at the middle itself
        if arr[mid] == x:
            return mid

        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search(arr, low, mid - 1, x)

        # Else the element can only be present in right subarray
        else:
            return binary_search(arr, mid + 1, high, x)

    else:
        # Element is not present in the array
        return -1


y = [1, 4, 5, 7, 8, 9, 11, 24, 44, 67]
print(binary_search(y, 11))


# Binary Search in python


def binarySearch(array, x, low, high):

    # Repeat until the pointers low and high meet each other
    while low <= high:

        mid = low + (high - low)//2

        if array[mid] == x:
            return mid

        elif array[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1


array = [3, 4, 5, 6, 7, 8, 9]
x = 4

result = binarySearch(array, x, 0, len(array)-1)

if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
