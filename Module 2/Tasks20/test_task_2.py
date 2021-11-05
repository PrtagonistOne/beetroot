import Task_1
import unittest


class TestClass(unittest.TestCase):
    def test_file_opened(self):
        with Task_1.ContextManager('myapp.log', 'r') as f:
            print('Inside the suite ', f.counter)
        self.assertEqual(f.counter, 1, 'If file was opened successfully, the value should be equal to 1')

    def test_file_path_not_found(self):
        with Task_1.ContextManager('textxvsv.txt', 'r') as f:
            print('Inside the suite')
        self.assertEqual(f.counter, 1, 'If file was opened successfully, the value should be equal to 1')


if __name__ == '__main__':
    unittest.main()
