# How to check if a string is palindrome in a stack

class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()


my_instance = Stack()
string_input = input('Enter the string... ')

for character in string_input:
    my_instance.push(character)

reversed_text = ''
while not my_instance.is_empty():
    reversed_text = reversed_text + my_instance.pop()

if string_input == reversed_text:
    print("The string is a palindrome")
else:
    print("The string isn't a palindrome")
