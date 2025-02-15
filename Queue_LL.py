#Queue implementation using LL
class node:
    def _init_(self,data):
        self.data=data
        self.next=None
class queue:
    def _init_(self):
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
obj=queue()
while True:
    print("1.enqueue 2.dequeue 3.exit")
    choice=int(input("enter the choice"))
    if choice==1:
        data=int(input("enter the data"))
        obj.enqueue(data)
    elif choice==2:
        obj.dequeue()
    elif choice==3:
        break
    else:
        print("Invalid choice")
