class node:
    def _init_(self,data):
        self.data=data
        self.next=None
class SCLL:
    def _init_(self):
        self.head=None
        self.temp=None
    def create(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
            self.temp=newnode
            self.tail=newnode
        else:
            self.tail.next=newnode
            newnode.next=self.head
            self.tail=newnode
    def display(self):
        self.temp=self.head
        while self.temp.next!=self.head:
            print(self.temp.data,end=" ")
            self.temp=self.temp.next
        print(self.tail.data)
        print()
    def del_at_front(self):
        self.head=self.head.next
        self.tail.next=self.head
    def del_at_end(self):
        self.temp=self.head
        while self.temp.next.next!=self.head:
            self.temp=self.temp.next
        self.temp.next.next=None
        self.temp.next=self.head
        self.tail=self.temp
    def del_at_mid(self,pos):
        self.temp=self.head
        i=1
        while i<pos-1:
            self.temp=self.temp.next
            i+=1
        self.temp=self.temp.next.next
        self.temp.next.next=None
        self.temp.next=self.temp
        

obj=SCLL()
while 1:
    choice=int(input("1.create 2.display 3.delete_in_front 4.delete_in_end 5.delete_in_mid 6.exit :"))
    if choice==1:
        data=int(input("enter data:"))
        obj.create(data)
    elif choice==2:
        obj.display()
    elif choice==3:
        obj.del_at_front()
    elif choice==4:
        obj.del_at_end()
    elif choice==5:
        pos=int(input("enter position to delete:"))
        obj.del_at_mid(pos)
    elif choice==6:
        break
