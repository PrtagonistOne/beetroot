from test import Node_1


class UnorderedList:

    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def append(self, item):
        temp = Node_1(item)
        temp.set_next(self._head)
        self._head = temp

    def size(self):
        current = self._head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def my_while_generator(self):
        current = self._head
        while current is not None:
            yield current.get_data()
            current = current.get_next()

    def index(self, item, start=0, end=None):
        temp_list = [i for i in self.my_while_generator()]
        if end is None:
            end = len(temp_list)
        value = [i for i in range(start, end) if temp_list[i] == item]
        if bool(value) is False:
            raise ValueError('Item was not found')
        return f"The index of {item} is {value}"

    def pop(self, index=-1):
        temp_list = [i for i in self.my_while_generator()]
        item = temp_list[index]
        self.remove(item)
        return item

    def insert(self, elem, i=0):
        temp_list = [i for i in self.my_while_generator()]
        temp_list.insert(i, elem)
        current = self._head
        for i in temp_list:
            if current is None:
                break
            print(i)
            current.data = i
            current = current.get_next()
        return temp_list

    def search(self, item):
        current = self._head
        found = False
        while current is not None and not found:
            if current.get_data() == item:
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self._head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self._head = current.get_next()
        else:
            previous.set_next(current.get_next())

    def __repr__(self):
        representation = "<UnorderedList: "
        current = self._head
        while current is not None:
            representation += f"{current.get_data()} "
            current = current.get_next()
        return representation + ">"

    def __str__(self):
        return self.__repr__()

unlist = UnorderedList()

[unlist.append(i) for i in [1, 3, 5, 6, 7, 10, 12]]
print(unlist)
print(unlist.index(1))
print(unlist.pop(), unlist.pop(0))
print(unlist)
print(unlist.insert(1))
print(unlist)