class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LL:
    def __init__(self):
        self.head = None

    def PrintLL(self):
        if self.head == None:
            print("Linked list is empty")
        else:
            curr = self.head
            while curr is not None:
                print(curr.data)
                curr = curr.next

    def addAtBegin(self,data):
        newNode = node(data)
        newNode.next = self.head
        self.head = newNode

    '''def addAtLast(self, data):
        newNode = node(data)
        curr = self.head
        while curr.next is not None:'''



list1= LL()
list1.addAtBegin(10)
list1.addAtBegin(100)
list1.addAtBegin(1000)
list1.addAtBegin(10000)
list1.PrintLL()

