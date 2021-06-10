# This is how you implement linear search for an ordered array

# Normal linear search
def linear_search(array, value):
    for i in range(len(array)):
        if i == value:
            return value
        elif i > value:
            break

    return None


# Ordered array linear search
def ordered_linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1
