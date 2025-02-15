#circular queue implementation 
class circular_queue:
    def __init__(self,size):
        self.size=size
        self.queue=[0]*size
        self.front=-1
        self.rear=-1
    def enqueue_rear(self, data):
        if self.rear+1==self.front or (self.front==0 and self.rear==self.size-1):
            print("Queue if full")
        elif self.rear ==-1 and self.front==-1:
            self.rear=self.front=0
            self.queue[self.rear]=data
        elif self.rear==self.size-1:
            self.rear=0
            self.queue[self.rear]=data
        else:
            self.rear+=1
            self.queue[self.rear]=data
    def enqueue_front(self,data):
        if self.rear+1==self.front or (self.front==0 and self.rear==self.size-1):
           print("Queue if full")
        elif self.rear ==-1 and self.front==-1:
            self.rear=self.front=0
            self.queue[self.front]=data
        elif self.front==0:
           self.front=self.size-1
           self.queue[self.front]=data
        else:
           self.front-=1
           self.queue[self.front]=data
    def dequeue_front(self):
        if self.front==-1 and self.rear==-1:
            print("queue is empty")
        elif self.front==self.rear:
            print(f"The deleted element: {self.queue[self.front]}")
            self.front=self.rear=-1
        elif self.front==self.size-1:
            print(f"The deleted element: {self.queue[self.front]}")
            self.front=0
        else:
            print(f"The deleted element: {self.queue[self.front]}")
            self.front+=1
    def dequeue_rear(self):
        if self.front==-1 and self.rear==-1:
            print("queue is empty")
        elif self.front==self.rear:
            print(f"The deleted element: {self.queue[self.rear]}")
            self.front=self.rear=-1
        elif self.rear==0:
            print(f"The deleted element: {self.queue[self.rear]}")
            self.rear=self.size-1
        else:
            print(f"The deleted element: {self.queue[self.rear]}")
            self.rear-=1
    def display(self):
        temp=self.front
        print("The queue elements are :",end=' ')
        while temp!=self.rear:
            print(self.queue[temp],end=' ')
            temp=(temp+1)%self.size
        print(self.queue[temp])
size =int(input("Enter the size"))
obj=circular_queue(size)
while True:
    print("1.enqueue_rear 2.enqueue_front 3.dequeue_front 4.dequeue_rear 5.display 6.exit")
    choice=int(input("Enter the choice "))
    if choice==1:
        data=int(input("Enter the data "))
        obj.enqueue_rear(data)
    elif choice==2:
        data=int(input("Enter the data"))
        obj.enqueue_front(data)
    elif choice==3:
        obj.dequeue_front()
    elif choice==4:
        obj.dequeue_rear()
    elif choice==5:
        obj.display()
    elif choice==6:
        break
