from typing import List


class WorkerClean:
    pass


class Boss:

    def __init__(self, id_: int, name: str, company: str, workers: List[WorkerClean]):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = workers

    @property
    def get_workers(self) -> list:
        return self.workers

    def add_worker(self, worker) -> None:
        self.workers.append(worker)
        print(f'A new worker "{worker}" was added!')

    def __str__(self) -> str:
        return f'id: {self.id}, name: {self.name}'

    def __repr__(self) -> str:
        return Boss.__str__(self)


class Worker(WorkerClean):
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

    def __str__(self) -> str:
        return f'id: {self.id}, name: {self.name}'

    def __repr__(self) -> str:
        return Worker.__str__(self)
