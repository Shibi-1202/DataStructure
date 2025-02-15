#Stack implementation
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
            print(f"Element {data} pushed onto stack")
    
    def pop(self):
        if self.top == -1: 
            print("Stack is empty")
            return None
        else:
            item = self.stack[self.top]
            self.top -= 1
            return item
    
    def peek(self):
        if self.top == -1:
            print("Stack is empty")
        else:
            print(f"The top element is {self.stack[self.top]}")
            
size = int(input("Enter the size of the stack: "))
obj = Stack(size)
while True:
    print("1. Push 2. Pop 3. Peek 4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter the data to push: "))
        obj.push(data)
    elif choice == 2:
        popped_item = obj.pop()
        if popped_item is not None:
            print(f"Popped element: {popped_item}")
    elif choice == 3:
        obj.peek()
    elif choice == 4:
        break
    else:
        print("Invalid choice, please try again.")

