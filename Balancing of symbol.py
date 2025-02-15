class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [0] * size
        self.top = -1 
    def push(self, data):
        if self.top == self.size - 1: 
            print("Stack is full")
        else:
            self.top += 1
            self.stack[self.top] = data
    def pop(self):
        if self.top == -1: 
            return None 
        else:
            item = self.stack[self.top]
            self.top -= 1
            return item
    def peek(self):
        if self.top == -1:
            return None
        else:
            return self.stack[self.top]
    def is_matching_pair(self, char, top):
        if char == ')' and top != '(':
            return False
        if char == '}' and top != '{':
            return False
        if char == ']' and top != '[':
            return False
        return True
def is_balanced(expression):
    obj= Stack(len(expression))
    for char in expression:
        if char == '(' or char == '{' or char == '[':
            obj.push(char)
        elif char == ')' or char == '}' or char == ']':
            top = obj.pop()
            if top is None:
                return False
            if not obj.is_matching_pair(char, top):
                return False
    return obj.top == -1
    
expression = input("Enter the expression to check for balanced symbols: ")

if is_balanced(expression):
    print("The expression has balanced symbols.")
else:
    print("The expression does not have balanced symbols.")

