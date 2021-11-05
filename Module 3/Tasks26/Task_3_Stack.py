class Stack:
    def __init__(self):
        self._items = []

    def is_empty(self):
        return bool(self._items)

    def push(self, item):
        self._items.append(item)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[len(self._items) - 1]

    def size(self):
        return len(self._items)

    def __repr__(self):
        representation = "<Stack>\n"
        for ind, item in enumerate(reversed(self._items)):
            representation += f"{ind}: {str(item)}\n"
        return representation

    def __str__(self):
        return self.__repr__()

    def get_from_stack(self, e):
        for i, k in enumerate(reversed(self._items)):
            if k is e:
                return f'Element {e} was found at index {i}'
        raise ValueError("Element was not found")


s = Stack()
[s.push(i) for i in range(20)]
print(s.get_from_stack(19))
