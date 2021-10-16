'''
https://leetcode.com/problems/palindrome-linked-list/submissions/
'''
# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nums = []

        while head:
            nums.append(head.val)
            head = head.next

        l, r = 0, len(nums) - 1
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        return True


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = head


def isPalindromeList(list):
    length = 0
    temp = list.head
    while temp:
        length += 1
        temp = temp.next
    left = list.head
    for i in range(length//2):
        right = list.head
        for j in range(length-i-1):
            right = right.next
        if left.data != right.data:
            return False
        left = left.next
    return True
