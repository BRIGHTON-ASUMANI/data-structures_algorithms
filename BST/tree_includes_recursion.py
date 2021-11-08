# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):
    if root == None: return False
    if root.val == target:
      return True
    return tree_includes(root.left, target) or tree_includes(root.right, target)