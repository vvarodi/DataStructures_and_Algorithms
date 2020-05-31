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

    def addLast(self, item):
        current = self.head
        while current is not None:
            current = current.next
        current.next = Node(item)

    def len(self):  # size
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

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.data == item:
                found = True
            else:
                previous = current
                current = current.next
        if previous is None:
            self.head = current.next  # removing the first node
        else:
            previous.next = current.next


mylist = SinglyLinkedList()
print(mylist.isEmpty())
print(mylist.addFirst('first'))
print(mylist.addFirst('sec'))
print(mylist.addFirst('last'))
print(mylist.head.next.data)
print(mylist.len())
print(mylist.search('first'))
print(mylist.head.next.data)
mylist.remove('sec')
print(mylist.head.next.data)
