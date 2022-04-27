#insert at a node 
class Node :
    def __init__(self,data,next):
        self.data=data
        self.next=next
class LinkedList:
    head =None
    def insertAtbegining(self,data):
        node=Node(data,self.head)
        self.head=node
    def print(self):
        if self.head is None:
            print("linkList is empty")
            return
        ltsr=''
        itr=self.head
        while itr:
            ltsr+=str(itr.data)
            itr=itr.next
        print(ltsr)
    def insert_At_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr:
            itr=itr.next
        itr.next=Node(data,None)
    def get_length(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    def remove_At(self,index):
        if index <0 or index>=self.get_length():
            raise Exception("invalid index")



        
        
if __name__ =='__main__':
    lt=LinkedList()
    lt.insertAtbegining(1)
    lt.insertAtbegining(2)
    lt.print()
