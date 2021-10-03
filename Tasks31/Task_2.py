from test import BinHeap


class PriorityQueue(BinHeap):
    def __init__(self, elems):
        super().__init__()
        self.elems = [i[0] for i in elems]
        self.values = [i for i in elems]
        self.b = BinHeap()

        self.values.insert(0, (0, None))
        self.b.build_heap(self.elems)

    def enqueue(self, tup) -> None:
        self.b.insert(tup[0])
        self.values.append(tup)

    def dequeue(self):
        val = [self.b.del_min() for i in range(len(self.values) - 1)]
        val.insert(0, 0)
        for i in range(len(val)):
            for j in range(len(self.values)):
                if self.values[j][0] == val[i]:
                    print(self.values[j], end=" ")


list_stu = [(5, 'Rina'), (1, 'Anish'), (3, 'Moana'), (2, 'cathy'), (4, 'Lucy')]
pr = PriorityQueue(list_stu)
pr.enqueue((7, 'Sasha'))
pr.dequeue()
print()
