
class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def bfs(root):
    queue = [root]
    i = 0
    while i < len(queue):
        poppedNode = queue[i]
        i += 1
        if poppedNode is None:
            continue
        else:
            poppedNode.left, poppedNode.right = poppedNode.right, poppedNode.left
            print(poppedNode.data)
            queue.append(poppedNode.left)
            queue.append(poppedNode.right)
