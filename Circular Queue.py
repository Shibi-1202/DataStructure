 #Circular_queue implementation
class circular_queue:
    def __init__(self,size):
        self.size=size
        self.queue=[0]*size
        self.front=-1
        self.rear=-1
    def enqueue(self,data):
        if (self.rear+1)%self.size==self.front:
            print("Queue is full")
        elif self.rear==-1 and self.front==-1:
            self.rear=self.front=0
            self.queue[self.rear]=data
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
    def dequeue(self):
        if self.rear==-1 and self.front==-1:
            print("Queue is empty")
        elif self.front==self.rear:
            print(f"The deleted element: {self.queue[self.front]}")
            self.rear=self.front=-1
        else:
            print(f"The deleted element: {self.queue[self.front]}")
            self.front=(self.front+1)%self.size
    def display(self):
        temp=self.front
        while temp!=self.rear:
            print(self.queue[temp],end=' ')
            temp=(temp+1)%self.size
        print(self.queue[temp])
size=int(input("Enter the size"))
obj=circular_queue(size)
while True:
    print("1.enqueue 2.dequeue 3.display 4.exit")
    choice=int(input("Enter the choice"))
    if choice==1:
        data=int(input("Enter the data"))
        obj.enqueue(data)
    elif choice==2:
        obj.dequeue()
    elif choice==3:
        obj.display()
    elif choice==4:
        obj.display()
    else:
        print("Invalid choice")
