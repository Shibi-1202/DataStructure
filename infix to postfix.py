class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0

def precedence(operator):
    if operator == '^':
        return 3
    elif operator in ('*', '/'):
        return 2
    elif operator in ('+', '-'):
        return 1
    return 0

def infix_to_postfix(expression):
    obj = Stack()
    result = []
    for char in expression:
        if char.isalnum():
            result.append(char)
        elif char == '(':
            obj.push(char)
        elif char == ')':
            while not obj.is_empty() and obj.stack[-1] != '(':
                result.append(obj.pop())
            obj.pop()
        else:
            while not obj.is_empty() and obj.stack[-1] != '(':
                top_operator = obj.pop()
                if precedence(top_operator) >= precedence(char) or (precedence(top_operator) == precedence(char) and char != '^'):
                    result.append(top_operator)
                else:
                    obj.push(top_operator)
                    break
            obj.push(char)
    while not obj.is_empty():
        result.append(obj.pop())
    return ''.join(result)

expression = input("Enter infix expression: ")
postfix_expression = infix_to_postfix(expression)
print(f"Postfix expression: {postfix_expression}")

