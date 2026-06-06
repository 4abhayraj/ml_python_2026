#singly linked list
#insertion at the end


class Node:
    #(self,info,next) => parameter
    def __init__(self,info,next=None): #this pointer in c, 
#whichever object created by init function, its address will be stroed in self named variable
        self.data = info # self will point oblect
        self.next = next 
class SinglyLinkedlist:
    def __init__(self,head=None): #no. of head == no. of singly linked list
        self.head = head

    def insertAtEnd(self,value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.head
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else :
            self.head = temp

    def insertAtBeg(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp


    def printLL(self):
        t1 = self.head
        while(t1.next != None):
            print(t1.data)
            t1 = t1.next
        print(t1.data)

obj = SinglyLinkedlist()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)

obj.insertAtBeg(5)

obj.printLL()


