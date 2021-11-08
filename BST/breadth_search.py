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
    result = []
    while i < len(queue):
        current = queue[i]
        i += 1
        if current is None:
            continue
        else:
            result.append(current.val)
            queue.append(current.left)
            queue.append(current.right)
    return result



# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None
from collections import deque

def breadth_first_values(root):
  if not root:
    return []
  
  queue = deque([ root ])
  values = []
  
  while queue:
    node = queue.popleft()
    
    values.append(node.val)
    
    if node.left:
      queue.append(node.left)
      
    if node.right:
      queue.append(node.right)
      
  return values

