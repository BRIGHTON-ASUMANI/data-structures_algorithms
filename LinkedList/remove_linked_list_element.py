'''
Given the head of a linked list and an integer val, remove all the 
nodes of the linked list that has Node.val == val, and return the new head.
'''

'''
https://leetcode.com/problems/remove-linked-list-elements/
'''

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        cur, prev = head, dummy

        while cur:
            if cur.val == val:
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next
        return dummy.next
