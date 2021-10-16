# Parameters:
#  arr: List[int]
# return type: int
'''
Description
Given a non-empty array of integers arr, create a function that returns the index of a peak element. We consider an element as peak if it's greater than or equal to its neighbors, the next and previous element (assume that arr[-1] and arr[n] are equal to -∞). And if there are multiple peaks in arr, just return the index of one of them.

Example 1:
Input: arr = [4, 5, 8, 3]
Output: 2
Explanation: arr[2] is a peak element because it's greater than or equal to arr[1], and greater than or equal to arr[3]
Example 2:
Input: arr = [1, 3, 4, 7, 8]
Output: 4
Explanation: arr[4] is a peak element because it's greater than or equal to arr[3], which is it's only neighbor
Example 3:
Input: arr = [1, 5, 2, 6, 6, 3]
Output: 3
Explanation: arr[3] is a peak element because it's greater than or equal to arr[2] and greater than or equal to arr[4] (other valid outputs would be 1 and 4, because arr[1] and arr[4] are also peak elements)

'''


import test


def findPeak(arr):
    n = len(arr)
    for i in range(n):
        if(i == 0 or arr[i] >= arr[i-1]) and (i == n-1 or arr[i] >= arr[i+1]):
            return i

    return 0


# Parameters:
#  arr: List[int]
# return type: int


# Binary search
def findPeak(arr):
    l, r, m = 0, len(arr)-1, 0
    while l < r:
        m = (l+r)//2
        if(arr[m] < arr[m+1]):
            l = m+1
        else:
            r = m
    return l
