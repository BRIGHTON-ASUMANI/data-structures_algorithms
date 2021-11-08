# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_sum(root):
  if root == None: return False
  total = 0
  stack = [root]
  while len(stack)>0:
    current = stack.pop()
    total +=current.val
    if current.right: stack.append(current.right)
    if current.left: stack.append(current.left)
  return total