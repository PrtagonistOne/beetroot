class Queue:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Queue>\n"
        for ind, item in enumerate(reversed(self._items)):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

    def get_from_queue(self, e):
        for i, k in enumerate(reversed(self._items)):
            if k is e:
                return f'Element {e} was found at index {i}'
        raise ValueError("Element was not found")


q = Queue()
[q.enqueue(i) for i in range(20)]

print(q.get_from_queue(19))
