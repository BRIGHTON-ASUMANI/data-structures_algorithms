'''
https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem?isFullScreen=true
'''


def printLinkedList(head):
    while head:
        print(head.data)
        head = head.next
