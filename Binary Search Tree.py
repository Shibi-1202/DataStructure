#Binary Search tree implementation
class node:
    def _init_(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
    def _init_(self):
        self.root =None
    def create(self,data):
        newnode=node(data)
        if self.root is None:
            self.root=newnode
        else:
            temp=self.root
            while True:
                if data<temp.data:
                    if temp.left is None:
                        temp.left=newnode
                        break
                    else:
                        temp=temp.left
                else:
                    if temp.right is None:
                        temp.right=newnode
                        break
                    else:
                        temp=temp.right
    def inorder(self,temp):
        if temp is not None:
            self.inorder(temp.left)
            print(temp.data,end=' ')
            self.inorder(temp.right)
obj=tree()
while True:
    print("1.create 2.inorder 3.exit")
    choice=int(input("Enter the choice"))
    if choice==1:
        data=int(input("Enter the data"))
        obj.create(data)
    elif choice==2:
        obj.inorder(obj.root)
    elif choice==3:
        break
    else:
        print("Invalid")
