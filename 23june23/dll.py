class Node:
    def __init__(self,data):
        self.previous=None
        self.data=data
        self.next=None
class Dll:
    def __init__(self):
        self.head=None
    def display(self):
        if self.head is None:
            print("double ll is empty")
        else:
            temp=self.head
            while temp:
                if temp.next!=None:
                    print(temp.data,"->",end=" ")
                else:
                    print(temp.data,end=" ")
                temp=temp.next
    def insert_begin(self,data):
        new_Node=Node(data)
        temp=self.head
        temp.previous=new_Node
        new_Node.next=temp
        self.head=new_Node
    def insert_end(self,data):
        new_Node=Node(data)
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_Node
        new_Node.previous=temp
    def insert_pos(self,pos,data):
        new_Node=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
        new_Node.previous=temp
        new_Node.next=temp.next
        temp.next.prev=new_Node
        temp.next=new_Node
    def delete_begin(self):
        temp=self.head
        self.head=temp.next
        temp.next.previous=None
        temp.next=None
    def delete_end(self):
        prev=self.head
        temp=self.head.next
        while temp.next is not None:
            temp=temp.next
            prev=prev.next
        prev.next=None
        temp.prev=None
    def delete_position(self,pos):
        prev=self.head
        temp=self.head.next
        for i in range(1,pos-1):
            temp=temp.next
            prev=prev.next
        prev.next=temp.next
        temp.prev=prev
        #temp.next=temp.prev

Node_1=Node("asha")
print(Node_1.data)
dl=Dll()
dl.head=Node_1
Node_2=Node("rishi")
Node_1.next=Node_2
Node_2.previous=Node_1
'''print(Node_1)
print(Node_2)
print(Node_1.next)
print(Node_2.previous)'''
print(Node_2.data)
Node_3=Node("anuhya")
Node_2.next=Node_3
Node_3.previous=Node_2
print(Node_3.data)
Node_4=Node("ananya")
Node_3.next=Node_4
Node_4.previous=Node_3
print(Node_4.data)
Node_5=Node("yochana")
Node_4.next=Node_5
Node_5.previous=Node_4
print(Node_5.data)
dl.insert_begin("uma")
dl.insert_end("ankitha")
dl.insert_pos(5,"teju")
dl.delete_begin()
dl.delete_end()
dl.delete_position(3)
dl.display()