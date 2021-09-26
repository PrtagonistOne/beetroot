from test import LinkedList


class Stack:
    def __init__(self):
        self._items = LinkedList()

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.add(item)

    def remove(self, data):
        return self._items.remove(data)

    def __str__(self):
        return self.__repr__()
