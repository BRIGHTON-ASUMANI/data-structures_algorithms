# Definition for singly-linked list.
'''
https://leetcode.com/problems/middle-of-the-linked-list/submissions/
'''


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        # Iterate till fast's next is null (fast reaches end)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # return the slow's data, which would be the middle element.
        print("The middle element is ", slow.val)
        return slow
