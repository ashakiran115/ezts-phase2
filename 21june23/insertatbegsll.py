class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SLL:
    def _init_(self):
        self.head=None
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            temp=self.head
            while temp:
                if temp.next!=None:
                    print(temp.data,"->",end=" ")
                else:
                    print(temp.data,end=" ")
                temp=temp.next
obj=SLL()
n=Node(10)
obj.head=n
n1=Node(20)
obj.head.next=n1
n2=Node(30)
n1.next=n2
n3=Node(40)
n2.next=n3
n4=Node(50)
n3.next=n4
n5=Node(60)
n4.next=n5
obj.display()
print("")
obj.insert_beginning(100)
obj.display()
print("")
print(obj.head.data)