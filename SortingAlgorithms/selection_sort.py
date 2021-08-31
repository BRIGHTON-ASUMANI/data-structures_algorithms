'''
Steps
- Find the smallest element in the array and swap it with the first element.
- Find the second smallest element and swap with with the second element in the array.
- Find the third smallest element and swap wit with the third element in the array.
- Repeat the process of finding the next smallest element and swapping it 
  into the correct position until the entire array is sorted.

- Space Complexity:  O(n)
- Time Complexity:  O(n2)
- Sorting in Place:  Yes
- Stable:  No
'''


def seletion_sort(arr):
    if not arr:
        return arr
    for i in range(len(arr)):
        min_i = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_i]:
                min_i = j
        arr[i], arr[min_i] = arr[min_i], arr[i]


'''
Javascript

function selectionSort(array) {
    for(var i = 0; i < array.length; i++) {
        var lowestNumberIndex = i;
        for(var j = i + 1; j < array.length; j++) {
            if(array[j] < array[lowestNumberIndex]) {
            lowestNumberIndex = j;
    }
}
    if(lowestNumberIndex != i) {
        var temp = array[i];
         array[i] = array[lowestNumberIndex];
        array[lowestNumberIndex] = temp;
        }
    }
    return array;
}

Let’s break this down. We’ll first present the line of code, followed by its
explanation.
    for(var i = 0; i < array.length; i++) {
Here, we have an outer loop that represents each passthrough of Selection
Sort. We then begin keeping track of the index containing the lowest value
we encounter so far with:
    var lowestNumberIndex = i;
which sets lowestNumberIndex to be whatever index i represents. Note that
we’re actually tracking the index of the lowest number instead of the actual
number itself. This index will be 0 at the beginning of the first passthrough,
1 at the beginning of the second, and so on.
    for(var j = i + 1; j < array.length; j++) {
kicks off an inner for loop that starts at i + 1 .
    if(array[j] < array[lowestNumberIndex]) {
    lowestNumberIndex = j;
    }
checks each element of the array that has not yet been sorted and looks for
the lowest number. It does this by keeping track of the index of the lowest
number it found so far in the lowestNumberIndex variable.
By the end of the inner loop, we’ve determined the index of the lowest
number not yet sorted.
    if(lowestNumberIndex != i) {
    var temp = array[i];
    array[i] = array[lowestNumberIndex];
    array[lowestNumberIndex] = temp;
    }
We then check to see if this lowest number is already in its correct place ( i ).
If not, we swap the lowest number with the number that’s in the position
that the lowest number should be at.
'''
