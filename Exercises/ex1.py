'''
Given an array of integers and a value,
determine if there are any two integers in the array whose sum is equal to the given value.
'''
nums = [1, 2, 3, 4, 5, 6, 7, 9]


def find_sum_of_two(nums, val):
    found_values = set()
    for a in nums:
        if val - a in found_values:
            return True

        found_values.add(a)

    return False


v = [5, 7, 1, 2, 8, 4, 3]
test = [3, 20, 1, 2, 7]

for i in range(len(test)):
    output = find_sum_of_two(v, test[i])
    print("find_sum_of_two(v, " + str(test[i]) + ") = " + str(output))
