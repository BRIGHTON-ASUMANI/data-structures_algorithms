# This is how you implement linear search for an ordered array

# Normal linear search
def linear_search(array, value):
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1


# Ordered array linear search
def ordered_linear_search(array, value):
    for num in array:
        if num == value:
            return value

        elif num > value:
            break
       
    return None


y = [1, 2, 3, 5, 7, 8, 20, 23, 33, 44, 55, 5555]

print(ordered_linear_search(y, 55))
