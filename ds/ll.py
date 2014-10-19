class Node(object):
    def __init__(self, data, next_=None):
        self.data = data
        self.next = next_
    def __str__(self):
        temp = self
        data = ''
        while temp != None:
            data += str(temp.data) + '->' 
            temp = temp.next
        return data[:-2]
class LinkedList(object):
    def __init__(self, data=None):
        self.head = None
        if data != None:
            self.head = Node(data)
    def __str__(self):
        temp = self.head
        data = ''
        while temp != None:
            data += str(temp.data) + '->' 
            temp = temp.next
        return data[:-2]
    def insert_front(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = Node(data, self.head)
            self.head = node
    def insert_back(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            head = self.head
            while head != None and head.next != None:
                head = head.next
            head.next = Node(data)
        

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_front(10)
    ll.insert_front(20)
    ll.insert_back(5)
    print ll
