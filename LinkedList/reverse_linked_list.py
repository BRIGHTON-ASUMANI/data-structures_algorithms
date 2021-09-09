'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
A linked list can be reversed either iteratively or recursively. Could you implement both
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


'''
iterative way
# Definition for singly-linked list.
'''


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


# recursion


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        newHead = head
        if head.next:
            newHead = self.reverseList(head.next)
            head.next.next = head

        head.next = None

        return newHead
