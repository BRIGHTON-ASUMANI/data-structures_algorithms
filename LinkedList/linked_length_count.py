"""
https://www.codewars.com/kata/55beec7dd347078289000021/train/python
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def length(node):
    # Your code goes here.
    if (node == None):
        return 0
    else:
        return 1 + length(node.next)


def count(node, data):
    # Your code goes here.
    if (node == None):
        return 0
    count = 0
    while node:
        if (node.data == data):
            count = count+1
        node = node.next

    return count

# option 2


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def length(node):
    leng = 0
    while node:
        leng += 1
        node = node.next
    return leng


def count(node, data):
    c = 0
    while node:
        if node.data == data:
            c += 1
        node = node.next
    return c

# option3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length(node):
    return 1 + length(node.next) if node else 0


def count(node, data):
    return (node.data == data) + count(node.next, data) if node else 0
