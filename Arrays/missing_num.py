'''
Given an array nums containing n distinct numbers in the range [0, n],
return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
'''


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_value = 0  # O(1)
        l_num = sorted(nums)[-1]  # O(n.logn)
        s_num = sorted(nums)[0]  # O(n.logn)
        range_values = range(s_num, l_num + 1)  # O(n)
        for x in range_values:  # O(n)
            if x not in nums:
                missing_value = x  # O(1)
        return missing_value  # O(n)


'''
The time complexity is O(n) since its linear time. Only one traversal of the array is needed.
Space Complexity is O(1). No extra space is needed
'''

# If you are using your own function to get the max and number in array
def min_and_max(x):
    minimum = maximum = x[0]
    for w in x[1:]:
        if w < minimum:
            minimum = w
        else:
            if w > maximum:
                maximum = w
    return (minimum, maximum)
