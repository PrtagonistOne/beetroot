class Boss:

    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []

    @property
    def get_workers(self) -> list:
        return self.workers

    def add_worker(self, worker):
        self.workers.append(worker)
        print(f'A new worker "{worker}" was added!')

    def __str__(self):
        return f'id: {self.id}, name: {self.name}'

    def __repr__(self):
        return Boss.__str__(self)


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss

    @property
    def get_boss(self) -> Boss:
        return self.boss

    @get_boss.setter
    def get_boss(self, boss: Boss) -> None:
        if isinstance(boss, Boss):
            self.boss = boss
            boss.workers.append(self)
            print('boss setter invoked')
        else:
            raise ValueError('You can pass only Boss objects')

    @get_boss.deleter
    def get_boss(self) -> None:
        print('Worker have moved to a different company\'s boss')
        del self.boss

    def __str__(self):
        return f'id: {self.id}, name: {self.name}'

    def __repr__(self):
        return Worker.__str__(self)


boss1 = Boss(1, 'Johny', 'Bethesda')
boss2 = Boss(2, 'Mike', 'Ubisoft')

worker1 = Worker(1, 'Marlo', 'Bethesda', boss1)
worker2 = Worker(2, 'Nika', 'Bethesda', boss1)
worker3 = Worker(3, 'Michael', 'Bethesda', boss1)

boss1.add_worker(worker1)
boss1.add_worker(worker2)
boss1.add_worker(worker3)

print(f'{boss1.name} has workers: {boss1.get_workers}\n')
del boss1.workers[-1]
worker3.get_boss = boss2
print(f'{boss1.name} has workers: {boss1.get_workers}\n')
print(f'{boss2.name} has workers: {boss2.get_workers}\n')
