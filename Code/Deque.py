class Deque:
    def __init__(self):
        self.items = []

    def addFirst(self, item):
        self.items.insert(0, item)

    def addLast(self, item):
        self.items.append(item)

    def removeFirst(self):
        if self.isEmpty():
            print('Error: Deque is empty')
            return None
        return self.items.pop(0)

    def removeLast(self):
        if self.isEmpty():
            print('Error: Deque is empty')
            return None
        return self.items.pop()

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

    def __str__(self):
        return str(self.items)
