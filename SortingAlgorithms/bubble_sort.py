'''
The Efficiency of Bubble Sort
The Bubble Sort algorithm contains two kinds of steps:
- Comparisons: two numbers are compared with one another to
determine which is greater.
- Swaps: two numbers are swapped with one another in order to sort
them.

Therefore, in Big O Notation, we would say that Bubble Sort has an
efficiency of O(N*N) which is also referred to as quadratic time.
'''


def bubble_sort(list):
    '''
    We keep track of up to which index is still unsorted with the
    unsorted_until_index variable. At the beginning, the array is totally unsorted,
    so we initialize this variable to be the final index in the array.
    '''
    unsorted_until_index = len(list) - 1
    '''
    We also create a sorted variable that will allow us to keep track whether the
    array is fully sorted. Of course, when our code first runs, it isn’t.
    '''
    sorted = False

    '''
    We begin a while loop that will last as long as the array is not sorted. Next,
    we preliminarily establish sorted to be True . We’ll change this back to False
    as soon as we have to make any swaps. If we get through an entire
    passthrough without having to make any swaps, we’ll know that the array is
    completely sorted.
    '''
    while not sorted:
        sorted = True
        '''
        Within the while loop, we begin a for loop that starts from the beginning of
        the array and goes until the index that has not yet been sorted. Within this
        loop, we compare every pair of adjacent values, and swap them if they’re
        out of order. We also change sorted to False if we have to make a swap.
        '''
        for i in range(unsorted_until_index):
            if list[i] > list[i+1]:
                sorted = False
                list[i], list[i+1] = list[i+1], list[i]
        '''
        By this line of code, we’ve completed another passthrough, and can safely
        assume that the value we’ve bubbled up to the right is now in its correct
        position. Because of this, we decrement the unsorted_until_index by 1, since
        the index it was already pointing to is now sorted.
        '''
        unsorted_until_index = unsorted_until_index - 1


def bubble_sort_2(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# list = [65, 55, 45, 35, 25, 15, 10]
# bubble_sort(list)
# print(list)


'''
Check for duplicates using bubble sort
Note: If you print number of steps below you find out
that it is length of array squared hence O(N*N). If the array is not duplicate
'''


def bubble_sort_duplicates(arr):
    n = len(arr)
    steps = 0
    for i in range(n):
        for j in range(0, n):
            steps += 1
            if(i != j and arr[i] == arr[j]):
                return True
    print(steps)
    return False


# list = [65, 55, 34, 25, 15, 10]
# print(bubble_sort_duplicates(list))

'''
A better way to optimize out bubble_sort_duplicates function
would be as below so that it takes O(N) in Javascript
'''

'''
This implementation uses a single loop, and keeps track of which numbers
it has already encountered using an array called existingNumbers . It uses this
array in an interesting way: every time the code encounters a new number,
it stores the value 1 inside the index of the existingNumbers corresponding to
that number.

function hasDuplicateValue(array) {
    var steps = 0;
    var existingNumbers = [];
    for(var i = 0; i < array.length; i++) {
        steps++;
        if(existingNumbers[array[i]] === undefined) {
            existingNumbers[array[i]] = 1;
        } else {
            return true;
        }
    }
    console.log(steps);
    return false;
}
'''
