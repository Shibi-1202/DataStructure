class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print("Pushed:",item)

    def pop(self):
        if self.is_empty():
            return "Stack Underflow!"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is Empty!"
        return self.stack[-1]

    def size(self):
        return len(self.stack)

    def display(self):
        if self.is_empty(): 
            print("Stack Underflow")
        else:
            print("The Stack is:",self.stack)


obj = Stack()
while True:
    print("\n\n1.Push\n2.Pop\n3.Peek\n4.Show Size\n5.Display\n6.Exit")
    choice = int(input("Enter a choice: "))
    if choice == 1:
        data = int(input("Enter data: "))
        obj.push(data)
    elif choice == 2:
        print("Popped:",obj.pop())
    elif choice == 3:
        print("Peeked:",obj.peek())
    elif choice == 4:
        print("Size of stack :",obj.size())
    elif choice == 5:
        obj.display()
    elif choice == 6:
        break
    else:
        print("Invalid Choice")
