'''
https://www.hackerrank.com/challenges/tree-top-view/problem?isFullScreen=true
'''


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


def topView(root):
    # Write your code here
    hm = {}
    queue = []
    queue.append((root, 0))
    while(queue):
        q = queue.pop(0)
        if q[1] not in hm:
            hm[q[1]] = q[0].info
        if q[0].left:
            queue.append((q[0].left, q[1]-1))
        if q[0].right:
            queue.append((q[0].right, q[1]+1))
    for k, v in sorted(hm.items()):
        print(str(v)+' ', end='')


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)
