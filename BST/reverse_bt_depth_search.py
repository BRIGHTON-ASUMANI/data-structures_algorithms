import test


class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

# Parameters:
#  root: Tree
# return type: void


def reverseTree(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left

    reverseTree(root.left)
    reverseTree(root.right)

    return root


outputs = []
for case in test.cases:
    root = test.copyTree(case.root)
    reverseTree(root)
    outputs.append(root)
test.result(outputs)




def reverseTree(self, root):
    q = deque()
    q.append(root)
    while q:
        node = q.popleft()
        if node:
            node.left, node.right = node.right, node.left
            q.append(node.left)
            q.append(node.right)
    return root