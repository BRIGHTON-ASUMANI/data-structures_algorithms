# Python program to implement delete operation in a
# sorted array

# /* Function to delete an element */
def deleteElement(arr, n, key):

    # Find position of element to be deleted
    pos = binarySearch(arr, 0, n - 1, key)

    if (pos == -1):
        print("Element not found")
        return n

    # Deleting element
    for i in range(pos, n - 1):
        arr[i] = arr[i + 1]

    return n - 1

# To search a ley to be deleted


def binarySearch(arr, low, high, key):

    if (high < low):
        return -1
    mid = (low + high) // 2

    if (key == arr[mid]):
        return mid
    if (key > arr[mid]):
        return binarySearch(arr, (mid + 1), high, key)

    return binarySearch(arr, low, (mid - 1), key)


# Driver code
arr = [10, 20, 30, 40, 50]

n = len(arr)
key = 30

print("Array before deletion")

for i in range(n):
    print(arr[i], end=" ")

n = deleteElement(arr, n, key)
print("\n\nArray after deletion")
for i in range(n):
    print(arr[i], end=" ")

# This code is contributed by shubhamsingh10
