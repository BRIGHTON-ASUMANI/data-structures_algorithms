matrix = [
    [1,  3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]

# target = 23: True
# target = 46: False

# Approach
# 1. Iterate over the larger array
# 2. For every item, do a binary search for the tar


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


def target_exists(matrix, target):
    for item in matrix:  # n
        if binary_search(item, target):  # log(n)
            return True

    return False


# Test cases, false, true, [],
print(target_exists(matrix, 0))


# Time - O(nm)
# Space - O(1)
