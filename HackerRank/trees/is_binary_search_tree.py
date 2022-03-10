'''
https://www.hackerrank.com/challenges/is-binary-search-tree/problem?isFullScreen=true
'''

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""


def check_binary_search_tree_(root):
    return check_BST_subtree(root, -1, 10001)


def check_BST_subtree(root, min_value, max_value):
    if(root == None):
        return True

    data = root.data

    if(min_value < data < max_value):
        return check_BST_subtree(root.left, min_value, data) and check_BST_subtree(root.right, data, max_value)
    else:
        return False
