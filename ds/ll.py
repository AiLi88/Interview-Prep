class Node(object):
    def __init__(self, data, next_=None):
        self.data = data
        self._next = next_
    def __str__(self):
        temp = self
        data = ''
        while temp != None:
            data += str(temp.data) + '->' 
            temp = temp._next
        return data[:-2]
def removeDuplications(head):
    temp = head


head = Node(10)
head._next = Node(12)
head._next._next = Node(13)
head._next._next._next = Node(10)
head._next._next._next._next = Node(10)
head._next._next._next._next._next = Node(11)


print head

removeDuplications(head)

print head
