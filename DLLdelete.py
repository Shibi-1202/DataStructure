class Node:
    def _init_(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def _init_(self):
        self.head = None
        self.temp = None
    def create(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            self.temp = self.head
            while self.temp.next is not None:
                self.temp = self.temp.next
            self.temp.next = newnode
            newnode.prev = self.temp
    
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
            if self.head.next is None:
                self.head = None
            else:
                self.head = self.head.next
                self.head.prev = None
    
    def del_at_mid(self, pos):
        if self.head is None:
            print("List is empty")
        else:
            self.temp = self.head
            i = 1
            while i < pos:
                self.temp = self.temp.next
                i += 1
            if self.temp.next is None:
                print("Position out of range")
            else:
                if self.temp.next.next is not None:
                    self.temp.next.next.prev = self.temp
                    self.temp.next = self.temp.next.next
    
    def del_at_end(self):
        if self.head is None:
            print("List is empty")
        else:
            self.temp = self.head
            while self.temp.next is not None:
                self.temp = self.temp.next
            if self.temp.prev is not None:
                self.temp.prev.next = None
            else:
                self.head = None

obj = DLL()
while True:
    print("1.create 2.display 3.delete_in_front 4.delete_in_mid 5.delete_in_end 6.exit")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        data = int(input("Enter the data: "))
        obj.create(data)
    elif choice == 2:
        obj.display()
    elif choice == 3:
        obj.del_at_front()
    elif choice == 4:
        pos = int(input("Enter position: "))
        obj.del_at_mid(pos)
    elif choice == 5:
        obj.del_at_end()
    elif choice == 6:
        break
    else:
        print("Invalid choice")
