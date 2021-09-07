import logging
from os import path

logging.basicConfig(filename='myapp.log', level=logging.INFO)


class ContextManager:
    counter = 0

    def __init__(self, file_path_or_name, mode):
        self.file_path = file_path_or_name
        self.mode = mode

        if not path.isfile(self.file_path):
            logging.error('FileNotFoundError')
        if self.mode not in ['r', 'w', 'x', 'a']:
            logging.error('ValueError')


    @classmethod
    def get_num(cls):
        logging.info('Counter value returned')
        return cls.counter

    def __enter__(self):
        logging.info('Entering context manager...')
        try:
            self.file = open(self.file_path, self.mode)
        except FileNotFoundError:
            ContextManager.counter -= 1
        ContextManager.counter += 1
        logging.info('Count value has been uncreased by 1')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f'Closing.....\nThe counter of context is {ContextManager.counter}')
        logging.info(f'The context manager just closed with counter value {ContextManager.counter}')
        ContextManager.counter = 0
        return None


if __name__ == "__main__":
    for i in range(4):
        with ContextManager('text.txt', 'r') as f:
            print(f'Inside the suite.. {f.counter} times..')

    print(ContextManager.get_num())