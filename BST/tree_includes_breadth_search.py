# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def tree_includes(root, target):
    queue = [root]
    i = 0
    while i < len(queue):
        current = queue[i]
        i += 1
        if current is None:
          continue
        if current.val == target:
          return True
        else:
            queue.append(current.left)
            queue.append(current.right)
    return False


# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.left = None
#     self.right = None

def breadth_first_values(root):
    if root == None: return []
    result = []
    queue = [root]
    i = 0
    while i<len(queue):
      current = queue[i]
      result.append(current.val)
      i+=1
      if current.left: queue.append(current.left)
      if current.right: queue.append(current.right)
    return result
    
    

