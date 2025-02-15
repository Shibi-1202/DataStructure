#Sll-implentation & insertion
class node:
        def __init__(self,data):
              self.data=data
              self.next=None
class SLL:
        size = 0
        def __init__(self):
              self.head=None
              self.temp=None

        def create(self,data):
              SLL.size += 1
              newnode=node(data)
              if self.head is None:
                      self.head=newnode
                      self.temp=self.head
              else:
                      self.temp.next=newnode
                      self.temp=newnode
        def display(self):
                self.temp=self.head
                while self.temp is not None:
                        print(self.temp.data,end=' ')
                        self.temp=self.temp.next
                print()
        def insert_at_front(self,data):
                newnode=node(data)
                newnode.next=self.head
                self.head=newnode
        def insert_at_mid(self,data,pos):
                newnode=node(data)
                i=1
                self.temp=self.head
                while i<pos-1:
                        self.temp=self.temp.next
                        i=i+1
                        print(i)
                newnode.next=self.temp.next
                self.temp.next=newnode
        def insert_at_end(self,data):
                newnode=node(data)
                self.temp=self.head
                while self.temp.next is not None:
                        self.temp=self.temp.next
                self.temp.next=newnode
        def bubblesort(self):
                self.temp = self.head
                bub = self.head
                i = 0
                while i < SLL.size :
                        while self.temp is not None:
                                if(bub.data > bub.next.data):
                                        bub.data , bub.next.data = bub.next.data,bub.data
                                self.temp = self.temp.next
                        i += 1
                self.display()

obj=SLL()
while(1):
        print("1.create 2.display 3.exit 4.insert_front 5.insert_mid 6.insert_end 7.sort")
        choice=int(input("enter the choice: "))
        if choice==1:
                data=int(input("enter the data"))
                obj.create(data)
        elif choice==2:
                obj.display()
        elif choice==3:
                break
        elif choice==4:
                data=int(input("enter the data"))
                obj.insert_at_front(data)
        elif choice==5:
                data=int(input("enter the data"))
                pos=int(input("enter position"))
                obj.insert_at_mid(data,pos)
        elif choice==6:
                data=int(input("enter the data"))
                obj.insert_at_end(data)
        elif choice == 7:
                obj.bubblesort()
        else:
                print("invalid choice")
