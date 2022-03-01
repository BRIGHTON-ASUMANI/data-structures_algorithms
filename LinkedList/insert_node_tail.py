'''
https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem?isFullScreen=true
'''


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)

    if (head == None):
        head = node
    else:
        current = head
        while (current.next != None):
            current = current.next
        current.next = node
    return head
