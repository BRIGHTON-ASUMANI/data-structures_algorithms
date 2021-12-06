# Linked list implementation in Python


class Node:
    # Creating a node
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None


if __name__ == '__main__':

    linked_list = LinkedList()

    # Assign item values
    linked_list.head = Node(1)
    second = Node(2)
    third = Node(3)
    count = 0

    # Connect nodes
    linked_list.head.next = second
    second.next = third

    # Print the linked list item
    while linked_list.head != None:
        count += 1
        print(linked_list.head.item, count)
        linked_list.head = linked_list.head.next


# A complete working Python program to demonstrate all
# insertion methods of linked list

# Node class
class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    # Functio to insert a new node at the beginning

    def push(self, new_data):

        # 1 & 2: Allocate the Node &
        #	 Put in the data
        new_node = Node(new_data)

        # 3. Make next of new Node as head
        new_node.next = self.head

        # 4. Move the head to point to new Node
        self.head = new_node

    # This function is in LinkedList class. Inserts a
    # new node after the given prev_node. This method is
    # defined inside LinkedList class shown above */

    def insertAfter(self, prev_node, new_data):

        # 1. check if the given prev_node exists
        if prev_node is None:
            print("The given previous node must inLinkedList.")
            return

        # 2. create new node &
        #	 Put in the data
        new_node = Node(new_data)

        # 4. Make next of new Node as next of prev_node
        new_node.next = prev_node.next

        # 5. make next of prev_node as new_node
        prev_node.next = new_node

    # This function is defined in Linked List class
    # Appends a new node at the end. This method is
    # defined inside LinkedList class shown above */

    def append(self, new_data):

        # 1. Create a new node
        # 2. Put in the data
        # 3. Set next as None
        new_node = Node(new_data)

        # 4. If the Linked List is empty, then make the
        # new node as head
        if self.head is None:
            self.head = new_node
            return

        # 5. Else traverse till the last node
        last = self.head
        while (last.next):
            last = last.next

        # 6. Change the next of last node
        last.next = new_node

    # Utility function to print the linked list

    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data)
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':

    # Start with the empty list
    llist = LinkedList()

    # Insert 6. So linked list becomes 6->None
    llist.append(6)

    # Insert 7 at the beginning. So linked list becomes 7->6->None
    llist.push(7)

    # Insert 1 at the beginning. So linked list becomes 1->7->6->None
    llist.push(1)

    # Insert 4 at the end. So linked list becomes 1->7->6->4->None
    llist.append(4)

    # Insert 8, after 7. So linked list becomes 1 -> 7-> 8-> 6-> 4-> None
    llist.insertAfter(llist.head.next, 8)

    print('Created linked list is:'),
    llist.printList()


# DELETE A LINKED LIST

# Python3 program to delete all
# the nodes of singly linked list

# Node class


class Node:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null


# Constructor to initialize the node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.head = None

    def deleteList(self):

        # initialize the current node
        current = self.head
        while current:
            prev = current.next  # move next node

            # delete the current node
            del current.data

            # set current equals prev node
            current = prev

        # In python garbage collection happens
        # therefore, only
        # self.head = None
        # would also delete the link list

    # push function to add node in front of llist
    def push(self, new_data):

        # Allocate the Node &
        # Put in the data
        new_node = Node(new_data)

        # Make next of new Node as head
        new_node.next = self.head

        # Move the head to point to new Node
        self.head = new_node


# Use push() to construct below
# list 1-> 12-> 1-> 4-> 1
if __name__ == '__main__':

    llist = LinkedList()
    llist.push(1)
    llist.push(4)
    llist.push(1)
    llist.push(12)
    llist.push(1)

    print("Deleting linked list")
    llist.deleteList()

    print("Linked list deleted")


# This article is provided by Shrikant13



# Python3 program to prlevel order traversal
# in spiral form using one queue and one stack.
 
# Representation of a Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = next
 
# Function to insert Node
def insert(root, item):
    temp = Node(0)
    temp.data = item
    temp.next = root
    root = temp
    return root
 
def display(root):
    while (root != None):
        print(root.data, end=" ")
        root = root.next
 
def arrayToList(arr, n):
    root = None
    for i in range(n - 1, -1, -1):
        root = insert(root, arr[i])
    return root
 
# Driver code
if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    root = arrayToList(arr, n)
    display(root)



