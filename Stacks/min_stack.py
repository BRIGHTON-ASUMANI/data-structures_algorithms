class MinStack():

    def __init__(self):
        self.element_stack = []
        self.min_element_stack = []

    def push(self, item):
        if self.is_empty():
            self.min_element_stack.append(item)
        else:
            min_element = min(self.min_element_stack[self.size() - 1], item)
            self.min_element_stack.append(min_element)
        self.element_stack.append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError('Empty stack')
        self.min_element_stack.pop()
        return self.element_stack.pop()

    def top(self):
        return self.element_stack[-1]

    def getMin(self):
        if self.is_empty():
            raise ValueError('Empty stack')
        return self.min_element_stack[self.size() - 1]

    def is_empty(self):
        return not self.size()

    def size(self):
        return len(self.element_stack)
