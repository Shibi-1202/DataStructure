#Stack linkedlist
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None 
    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        print(f"Element {data} pushed onto stack.")
    def pop(self):
        if self.top is None:
            print("Stack is empty, cannot pop.")
        else:
            temp = self.top
            self.top = self.top.next
            print(f"Popped element: {temp.data}")
            del temp
    def peek(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            print(f"The top element is {self.top.data}")
stack = Stack()
while True:
    print("1. Push 2. Pop 3. Peek 4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter the data to push: "))
        stack.push(data)
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.peek()
    elif choice == 4:
        break
    else:
        print("Invalid choice. Please try again.")

