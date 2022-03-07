# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_min_value(root):
    if root == None:
        return False
    smallest = float('inf')
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        if(current.val < smallest):
            smallest = current.val
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return smallest
