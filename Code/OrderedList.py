class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class OrderedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head is None

    def len(self):  # size
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def add(self, item):
        new = Node(item)
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.data > item:
                stop = True
            else:
                previous = current
                current = current.next
        if previous is None:
            new.next = self.head
            self.head = new
        else:
            new.next = current
            previous.next = new
        self.size += 1

    def search(self, item):
        current = self.head
        stop = False
        while current is not None and stop is False:
            if current.data == item:
                return True
            else:
                if current.data > item:
                    stop = True
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

mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.size)
print(mylist.search(93))
print(mylist.search(100))
