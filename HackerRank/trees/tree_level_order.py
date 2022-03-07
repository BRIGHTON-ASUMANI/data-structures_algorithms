'''
https://www.hackerrank.com/challenges/tree-level-order-traversal/problem?isFullScreen=true
'''
from collections import deque


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def levelOrder(root):
    # Write your code here
    if not root:
        return

    queue = deque()
    queue.append(root)
    while queue:
        el = queue.popleft()
        print(el.info, end=' ')
        if el.left:
            queue.append(el.left)
        if el.right:
            queue.append(el.right)


def levelOrder2(root):
    queue = [root]

    while(len(queue) > 0):
        current = queue.pop(0)
        print(current.info, end=" ")
        if (current.left != None):
            queue.append(current.left)
        if (current.right != None):
            queue.append(current.right)


def levelOrder3(root):
    # Write your code here
    if root == None:
        return
    queue = [root]
    i = 0
    while i < len(queue):
        current = queue[i]
        print(current.info, end=" ")
        i += 1
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    return 0
