class node:
    def _init_(self,data):
        self.data=data
        self.next=None
class stack:
    def _init_(self):
        self.top=None
    def push(self,data):
        newnode=node(data)
        newnode.next=self.top
        self.top=newnode
    def pop(self):
        if self.top ==None:
            print("Underflow")
        else:
            self.top=self.top.next
    def peek(self):
        print(self.top.data)
