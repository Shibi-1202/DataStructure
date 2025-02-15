#Binary  tree implementation
class node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class tree:
    def __init__(self):
        self.root =None
    def create(self,data):
        newnode=node(data)
        if self.root is None:
            self.root=newnode
        else:
            temp1=self.root
            temp2=self.root
            flag=0
            while True:
                if temp1.left is None:
                    temp1.left= newnode
                    break
                elif temp1.right is None:
                    temp1.right=newnode
                    break
                elif flag==0:
                    temp1=temp2.left
                    flag=1
                else:
                    temp1=temp2.right
                    flag=0
                    temp2=temp2.left
    def inorder(self,temp):
        if temp is not None:
            self.inorder(temp.left)
            print(temp.data,end=' ')
            self.inorder(temp.right)
    def preorder(self,temp):
        if temp is not None:
            print(temp.data,end=' ')
            self.inorder(temp.left)
            self.inorder(temp.right)
    def postorder(self,temp):
        if temp is not None:
            self.inorder(temp.left)
            self.inorder(temp.right)
            print(temp.data,end=' ')
obj=tree()
while True:
    print("1.create 2.inorder 3.preorder 4.postorder 5.exit")
    choice=int(input("Enter the choice"))
    if choice==1:
        data=int(input("Enter the data"))
        obj.create(data)
    elif choice==2:
        obj.inorder(obj.root)
    elif choice==3:
        obj.preorder(obj.root)
    elif choice==4:
        obj.postorder(obj.root)
    elif choice==5:
        break
    else:
        print("Invalid")
