# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def max_path_sum(root):
    smallest = float('-inf')
    if root is None:
      return smallest
    if root.left == None and root.right == None: return root.val
    left_values = max_path_sum(root.left)
    right_values = max_path_sum(root.right)
    return  root.val + max(left_values, right_values)
