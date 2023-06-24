queue=[]
def enqueue_element():
    if len(queue)==n:
        print("queue is full")
    else:
        element=input("enter the element to be inserted in the stack:")
        queue.append(element)
        print(queue)
def dequeue_element():
    if not queue:
        print("stack is empty,add an element")
    else:
        d=queue.pop(0)
        print(d,"removed")
        print(queue)
n=int(input("enter size of the queue:"))
while True:
    print("select the operation 1.enqueue,2.dequeue,3.quit:")
    choice=int(input())
    if choice==1:
        enqueue_element()
    elif choice==2:
        dequeue_element()
    elif choice==3:
        break
    else:
        print("enter correct number")