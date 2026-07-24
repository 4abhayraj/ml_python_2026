#singly linked list
#insertion at the end, Begining, middile, and delete


class Node:
    #(self,info,next) => parameter
    def __init__(self,info,next=None): #this pointer in c, 
#whichever object created by init function, its address will be stroed in self named variable
        self.data = info # self will point object
        self.next = next 
class SinglyLinkedlist:
    def __init__(self,head=None): #no. of head == no. of singly linked list
        self.head = head

    def insertAtEnd(self,value):
        temp = Node(value)
        if(self.head != None):
            t1 = self.headg
            while(t1.next != None):
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def insertAtBeg(self,value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

#x is data after which we want to add data
    def insertInMid(self,value,x): #x is value after which we want to add data (not index)
        temp =  Node(value)
        t1 = self.head #points first location

        while(t1.next != None):
            if(t1.data == x):
                temp.next = t1.next
                t1.next = temp
            t1 = t1.next

    def deleteLL(self,value):
        t1 = self.head
        prev = t1
        if(t1.data == value):
            self.head = t1.next
        while(t1.next != None):
            if(t1.data == value):
                prev.next = t1.next
                break
            else:
                prev = t1
                t1 = t1.next
    
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

obj.insertInMid(40,20) #insert 40 after 20

obj.deleteLL(20)

obj.printLL()


