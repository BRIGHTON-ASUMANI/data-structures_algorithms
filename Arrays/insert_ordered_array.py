# Python3 program to implement insert
# operation in an sorted array.

# Inserts a key in arr[] of given capacity.
# n is current size of arr[]. This function
# returns n+1 if insertion is successful, else n.
def insertSorted(arr, n, key, capacity):

    # Cannot insert more elements if n is
    # already more than or equal to capcity
    if (n >= capacity):
        return n

    i = n - 1
    while i >= 0 and arr[i] > key:
        arr[i + 1] = arr[i]
        i -= 1

    arr[i + 1] = key

    return (n + 1)


# Driver Code
arr = [12, 16, 20, 40, 50, 70]

for i in range(20):
    arr.append(0)

capacity = len(arr)
n = 6
key = 26

print("Before Insertion: ", end=" ")
for i in range(n):
    print(arr[i], end=" ")

# Inserting key
n = insertSorted(arr, n, key, capacity)

print("\nAfter Insertion: ", end="")
for i in range(n):
    print(arr[i], end=" ")

# This code is contributed by Mohit Kumar
