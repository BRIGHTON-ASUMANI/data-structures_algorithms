# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # do nothing if the list is empty
        if head is None:
            return None

        current = head

        # compare the current node with the next node
        while current.next:
            if current.val == current.next.val:
                nextNext = current.next.next
                current.next = nextNext
            else:
                current = current.next        # only advance if no deletion

        return head
