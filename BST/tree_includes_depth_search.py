# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):
    if root == None: return False
    stack = [root]

    while len(stack) > 0:
        current = stack.pop()
        if current.val == target:
          return True
        if current.right: stack.append(current.right)
        if current.left: stack.append(current.left)
    return False