# DLL - IMPLEMENTATION & INSERTION

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class DLL:
    count = 0
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,data):
        newnode=node(data)
        DLL.count += 1
        if self.head==None:
            self.head=newnode
            self.temp=self.head
        else:
            self.temp.next=newnode
            newnode.prev=self.temp
            self.temp=newnode
    def display_rev(self):
        self.temp=self.head
        while self.temp.next is not None:
            self.temp=self.temp.next
        while self.temp !=None:
            print(self.temp.data,end=' ')
            self.temp=self.temp.prev
        print()
        self.temp = self.head
    def display_front(self):
        self.temp=self.head
        while self.temp!=None:
            print(self.temp.data,end=' ')
            self.temp=self.temp.next
        print()
    def insert_at_front(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head.prev=newnode
        self.head=newnode
    def insert_at_mid(self,data):
        newnode=node(data)
        i=1
        self.temp=self.head
        while i<pos-1:
            self.temp=self.temp.next
            i=i+1
        newnode.next=self.temp.next
        newnode.prev=self.temp
        self.temp.next=newnode
        newnode.next.prev=newnode
    def insert_at_end(self,data):
        newnode=node(data)
        self.temp=self.head
        while self.temp.next is not None:
            self.temp=self.temp.next
        newnode.prev=self.temp
        self.temp.next=newnode
obj=DLL()
while(1):
    print("1.create 2.display_rev 3.exit 4.insert_at_front 5.insert_at_mid 6.insert_at_end 7.display_front 8.Count_of_Nodes")
    choice=int(input("enter the choice"))
    if choice==1:
        data=int(input("enter the data"))
        obj.create(data)
    elif choice==2:
        obj.display_rev()
    elif choice==3:
        break
    elif choice==4:
        data=int(input("enter the data"))
        obj.insert_at_front(data)
    elif choice==5:
        data=int(input("enter the data"))
        pos=int(input("enter the pos"))
        obj.insert_at_mid(data)
    elif choice==6:
        data=int(input("enter the data"))
        obj.insert_at_end(data)
    elif choice ==7:
        obj.display_front()
    elif choice == 8:
        print("No:of nodes are:",DLL.count)
    else:
        print("invalid")
