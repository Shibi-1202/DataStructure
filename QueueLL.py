#Queue implementation using LL
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class queue:
    def __init__(self):
        self.rear=None
        self.front=None
    def enqueue(self,data):
        newnode=node(data)
        if self.rear==None and self.front==None:
            self.rear=newnode
            self.front=newnode
        else:
            self.rear.next=newnode 
            self.rear=newnode
    def dequeue(self):
        if self.rear==None and self.front==None:
            print("Queue is empty")
        else:
            temp=self.front
            print(f"element: {self.front.data}")
            self.front=self.front.next
            del temp
            if self.front is None:
                self.rear=None

    def display(self):
        temp = self.front
        while temp is not None:
            print(temp.data, end = " ")
            temp = temp.next
        print()
obj=queue()
while True:
    print("1.enqueue 2.dequeue 3.Display 4.exit")
    choice=int(input("enter the choice"))
    if choice==1:
        data=int(input("enter the data"))
        obj.enqueue(data)
    elif choice==2:
        obj.dequeue()
    elif choice==3:
        obj.display()
    elif choice ==4:
        break
    else:
        print("Invalid choice")
