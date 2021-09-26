class Node_1:
    def __init__(self, data):
        self._data = data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, data):
        self._data = data

    def set_next(self, new_next):
        self._next = new_next


class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self, root=None):
        self.root = root
        self.size = 0

    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def __repr__(self):
        next_n = self.root
        res = ''

        while next_n:
            res += str(next_n.data) + ' -> '
            next_n = next_n.next_node
        return res

    def remove(self, data):
        this_node = self.root
        prev_node = None

        while this_node:
            if this_node.data == data:
                if prev_node:
                    prev_node.next_node = this_node.next_node
                else:
                    self.root = this_node.next_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.next_node
        return False
