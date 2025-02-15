#Queue implementation using array
class queue:
    def __init__(self,size):
        self.size=size
        self.queue=[0]*size
        self.front=-1
        self.rear=-1
    def enqueue(self,data):
        if self.rear == self.size-1:
            print("queue is full")
        elif self.rear==-1 and self.front==-1:
            self.rear=0
            self.front=0
            self.queue[self.rear]=data
        else:
            self.rear+=1
            self.queue[self.rear]=data
    def dequeue(self):
        if self.rear==-1 and self.front==-1:
            print("queue is empty")
            return None
        elif self.rear==self.front:
            item=self.queue[self.front]
            self.rear=-1 
            self.front=-1
        else:
            item=self.queue[self.front]
            self.front+=1
        return item
    def peek(self):
        print(f"The peek element is {self.front}-->{self.queue[self.front]}")

    def display(self):
        temp = self.front
        while temp != self.size:
            print(self.queue[temp],end = " ")
            temp +=1
        print()
size=int(input("enter the size"))
obj=queue(size)
while True:
    print("1.enqueue 2.dequeue 3.peek 4.exit")
    choice=int(input("enter the choice:"))
    if choice==1:
        data=int(input("enter the data"))
        obj.enqueue(data)
    elif choice==2:
        del_ele=obj.dequeue()
        print(f"The deleted element:{del_ele}")
    elif choice==3:
        obj.peek()
    elif choice==4:
        break
    elif choice == 5:
        obj.display()
    else:
        print("invalid choice")
