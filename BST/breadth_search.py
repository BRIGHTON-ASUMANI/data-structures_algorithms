'''
Tree breadth first search
Description
Given a binary tree root, create a function that prints its nodes in level order (level by level).

Example 1:
Input: root = [5, 10, 3, 4, 6, null, 7, null, 8, 9, 1, 2]
Output: 5 10 3 4 6 7 8 9 1 2

'''


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def bfs(root):
    queue = [root]
    i = 0
    while i < len(queue):
        poppedNode = queue[i]
        i += 1
        if poppedNode is None:
            continue
        else:
            print(poppedNode.data)
            queue.append(poppedNode.left)
            queue.append(poppedNode.right)
