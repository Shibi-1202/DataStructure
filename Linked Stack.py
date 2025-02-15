#linked list stack

class node:
    def __init__(self,data):
        self.next = None
        self.data = data

class LinkStack:
    def __init__(self):
        self.top = None
        
    def push(self,data):
        newnode = node(data)
        newnode.next = self.top
        self.top = newnode

    def pop(self):
        if self.top == None:
            print("Underflow")
        else:
            print("poped data:",self.top.data)
            self.top = self.top.next

    def peek(self):
        print("Peek Element:",self.top.data)
        
obj = LinkStack()
while 1:
    choice = int(input("1.push 2.pop 3.peek"))
    if(choice==1):
        data=int(input("Enter a data:"))
        obj.push(data)
    elif(choice==2):
        obj.pop()
    elif(choice==3):
        obj.peek()
