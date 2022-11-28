import test


class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Parameters:
#  root: Tree
# return type: None

# Insert Node

# Print the Tree


def PrintTree(self):
    if self.left:
        self.left.PrintTree()
    print(self.data),
    if self.right:
        self.right.PrintTree()


def insert(self, data):

    if self.data:
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
    else:
        self.data = data


def dfsPreorder(root):
    # your code here
    res = []
    if root:
        res.append(root.data)
        res = res + dfsPreorder(root.left)
        res = res + dfsPreorder(root.right)
    return res


def dfsInorder(root):
    res = []
    if root:
        res = res + dfsInorder(root.left)
        res.append(root.data)
        res = res + dfsInorder(root.right)
    return res


def dfsPostorder(root):
    res = []
    if root:
        res = res + dfsPostorder(root.left)
        res = res + dfsPostorder(root.right)
        res.append(root.data)
    return res


print("Preorder:")
print("Your output:")
dfsPreorder(test.copyTree(test.root))
test.preorder()
print("------------")
print("Inorder:")
print("Your output:")
dfsInorder(test.copyTree(test.root))
test.inorder()
print("------------")
print("Postorder:")
print("Your output:")
dfsPostorder(test.copyTree(test.root))
test.postorder()
