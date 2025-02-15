class node:
    def _init_(self, data):
        self.data = data
        self.next = None

class SLL:
    def _init_(self):
        self.head = None
        self.temp = None

    def create(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
            self.temp = newnode
        else:
            self.temp.next = newnode
            self.temp = newnode

    def display(self):
        self.temp = self.head
        while self.temp is not None:
            print(self.temp.data, end=' ')
            self.temp = self.temp.next
        print()

    def del_at_front(self):
        if self.head is None:
            print("List is empty")
        else:
            self.head = self.head.next

    def del_at_end(self):
        if self.head is None:
            print("List is empty")
        elif self.head.next is None:
            self.head = None
        else:
            self.temp = self.head
            while self.temp.next.next is not None:
                self.temp = self.temp.next
            self.temp.next = None

    def del_at_mid(self, pos):
        if self.head is None:
            print("List is empty")
        elif pos == 1:
            self.del_at_front()
        else:
            self.temp = self.head
            i = 1
            while i < pos - 1:
                self.temp = self.temp.next
                i += 1
            if self.temp.next is not None:
                self.temp.next = self.temp.next.next
            else:
                print("Position out of range")

obj = SLL()
while True:
    print("1.create 2.display 3.del_at_front 4.del_at_mid 5.del_at_end 6.exit")
    choice = int(input("enter the choice: "))
    if choice == 1:
        data = int(input("enter the data: "))
        obj.create(data)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.del_at_front()
    elif choice == 4:
        pos = int(input("enter the position to delete: "))
        obj.del_at_mid(pos)
    elif choice == 5:
        obj.del_at_end()
    elif choice == 6:
        break
    else:
        print("Give correct choice!")
