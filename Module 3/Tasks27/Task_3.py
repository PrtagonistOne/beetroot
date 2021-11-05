from test import LinkedList


class Queue:
    def __init__(self):
        self._items = LinkedList()

    def is_empty(self):
        return bool(self._items)

    def enqueue(self, item):
        self._items.add(item)

    def dequeue(self, data):
        return self._items.remove(data)

    def __str__(self):
        return self.__repr__()
