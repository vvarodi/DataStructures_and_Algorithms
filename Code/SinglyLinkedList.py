class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head is None

    def addFirst(self, item):
        temp = Node(item)
        temp.next = self.head
        self.head = temp
        self.size += 1

    def len(self): #size
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def search(self, item):
        current = self.head
        while current is not None:
            if current.data == item:
                return True
            current = current.next
        return False

mylist = SinglyLinkedList()
print(mylist.isEmpty())
print(mylist.addFirst('p1'))
print(mylist.addFirst('p2'))
print(mylist.addFirst('p3'))
print(mylist.head.next.data)
print(mylist.len())
print(mylist.search('p2'))