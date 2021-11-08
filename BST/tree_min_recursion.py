# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):
    if root.left == None and root.right == None: return root.val
    return min(root.val, tree_min_value(root.left), tree_min_value(root.right))