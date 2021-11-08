# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum(root):
  if root == None: return False
  total = 0
  queue = [root]
  i = 0
  while i<len(queue):
    current = queue[i]
    total +=current.val
    i+=1
    if current.right: queue.append(current.right)
    if current.left: queue.append(current.left)
  return total


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def breadth_first_values(root):
    if root == None: return 0
    total = 0
    queue = [root]
    i = 0
    while i<len(queue):
      current = queue[i]
      total += current.val
      i+=1
      if current.left: queue.append(current.left)
      if current.right: queue.append(current.right)
    return total
    
    

