# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):
    if root == None: return 0
    smallest = float('inf')
    queue = [root]
    i = 0
    while i<len(queue):
      current = queue[i]
      if(current.val < smallest):
        smallest = current.val
      i+=1
      if current.left: queue.append(current.left)
      if current.right: queue.append(current.right)
    return smallest