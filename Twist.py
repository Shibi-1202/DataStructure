class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)

    def display(self):
        for box in self.stack:
            print(box)

class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        if len(self.queue) < self.size:
            self.queue.append(item)
        else:
            print("Queue is full")

    def display(self):
        for i in range(len(self.queue)-1, -1, -1):
            print(self.queue[i])


def modify_stack(stack):
    primary_colors = {"Red", "Green", "Blue"}
    queue = Queue(stack.size())
    temp_stack = Stack()

    while not stack.is_empty():
        box = stack.pop()
        if box in primary_colors:
            temp_stack.push(box)
        else:
            queue.enqueue(box)

    # Restore the stack's original order
    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())

    return queue


n = int(input("Enter the number of boxes: "))

stack = Stack()
for _ in range(n):
    box = input()
    stack.push(box)

queue = modify_stack(stack)

print("Boxes in the stack after modification:")
stack.display()

print("\nBoxes in the queue:")
queue.display()