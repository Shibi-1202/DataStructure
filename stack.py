class stack:
    def __init__(self):
        self.top = -1
    def create(self,size):
        self.size=size
        self.array = [0] * size

    def push(self,data):
        if (self.top >= self.size-1):
            print("Stack overflow")
        else:
            self.top+=1
            self.array[self.top] = data

    def pop(self):
        if (self.top < 0):
            print("Stack Underflow")
        else:
            print(self.array[self.top])
            self.array[self.top] = 0
            self.top-=1

    def peek(self):
        print(self.array[self.top])

    def display(self):
        print("\n",self.array)

obj = stack()
while 1:
    choice = int(input("1.create stack\n2.push element\n3.pop element\n4.peek\n5.display\n6.exit\nEnter your choice: "))
    if (choice==1):
        size = int(input("Enter the size:"))
        obj.create(size)
    elif (choice==2):
        data = int(input("Enter a data:"))
        obj.push(data)
    elif (choice==3):
        obj.pop()
    elif (choice==4):
        obj.peek()
    elif (choice==5):
        obj.display()
    elif (choice==6):
        break
    else:
        print("Invalid choice, Try again\n")
        
        
        
