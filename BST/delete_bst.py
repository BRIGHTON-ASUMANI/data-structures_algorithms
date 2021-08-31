'''
Pulling all the steps together, the algorithm for deletion from a binary tree
is:
If the node being deleted has no children, simply delete it.
If the node being deleted has one child, delete it and plug the child into
the spot where the deleted node was.
When deleting a node with two children, replace the deleted node with
the successor node. The successor node is the child node whose valueis the least of all values that are greater than the deleted node.
If the successor node has a right child, after plugging the
successor node into the spot of the deleted node, take the right
child of the successor node and turn it into the left child of the
parent of the successor node.
Here’s a recursive Python implementation of deletion from a binary tree.
It’s a little tricky at first, so we’ve sprinkled comments liberally:
'''


def delete(valueToDelete, node):

    # The base case is when we've hit the bottom of the tree,
    # and the parent node has no children:
    if node is None:
        return None
    # If the value we're deleting is less or greater than the current node,
    # we set the left or right child respectively to be
    # the return value of a recursive call of this very method on the current
    # node's left or right subtree.
    elif valueToDelete < node.value:
        node.leftChild = delete(valueToDelete, node.leftChild)
        # We return the current node (and its subtree if existent) to
        # be used as the new value of its parent's left or right child:
        return node
    elif valueToDelete > node.value:
        node.rightChild = delete(valueToDelete, node.rightChild)
        return node
        # If the current node is the one we want to delete:
    elif valueToDelete == node.value:
        # If the current node has no left child, we delete it by
        # returning its right child (and its subtree if existent)
        # to be its parent's new subtree:
        if node.leftChild is None:
            return node.rightChild
        # (If the current node has no left OR right child, this ends up# being None as per the first line of code in this function.)
    elif node.rightChild is None:
        return node.leftChild
    # If the current node has two children, we delete the current node
    # by calling the lift function (below), which changes the current node's
    # value to the value of its successor node:
    else:
        node.rightChild = lift(node.rightChild, node)
        return node

    def lift(node, nodeToDelete):

        # If the current node of this function has a left child,
        # we recursively call this function to continue down
        # the left subtree to find the successor node.
        if node.leftChild:
            node.leftChild = lift(node.leftChild, nodeToDelete)
            return node
        # If the current node has no left child, that means the current node
        # of this function is the successor node, and we take its value
        # and make it the new value of the node that we're deleting:
        else:
            nodeToDelete.value = node.value
            # We return the successor node's right child to be now used
            # as its parent's left child:
            return node.rightChild


'''
Like search and insertion, deleting from trees is also typically O(log N).
This is because deletion requires a search plus a few extra steps to deal with
any hanging children. Contrast this with deleting a value from an ordered
array, which takes O(N) due to shifting elements to the left to close the gap
of the deleted value.

'''
