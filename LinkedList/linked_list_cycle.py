'''
https://leetcode.com/problems/linked-list-cycle/

https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle/problem?isFullScreen=true
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head

        while(slow and fast and fast.next):
            slow = slow.next
            fast = fast.next.next

            if(slow == fast):
                return slow
        return
