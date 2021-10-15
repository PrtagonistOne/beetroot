import operator
from typing import Generic, TypeVar, List
from oop_tree import BinaryTree
from io import StringIO
import sys
T = TypeVar("T")


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio  # free up some memory
        sys.stdout = self._stdout


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container  # not is true for empty container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()  # LIFO

    def __repr__(self) -> str:
        return repr(self._container)


def build_parse_tree(math_exp: str) -> BinaryTree:
    tokens_list = math_exp.split()
    stack = Stack()
    tree: BinaryTree = BinaryTree('')
    stack.push(tree)
    current_tree = tree

    for i in tokens_list:
        if i == '(':
            current_tree.insert_left('')
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()

        elif i in ['+', '-', '*', '/']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()

        elif i == ')':
            current_tree = stack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                current_tree.set_root_val(int(i))
                parent = stack.pop()
                current_tree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return tree


def evaluate(parse_tree):
    operates = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = operates[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.get_root_val()


def print_exp(tree: BinaryTree):
    s_val = ''

    if tree:

        s_val = '(' + print_exp(tree.get_left_child())
        s_val = s_val + str(tree.get_root_val())
        s_val = s_val + print_exp(tree.get_right_child()) + ')'
    if s_val.__len__() > 10:  # Выбрал 10 потому что это количество рекурсий в смысле в стеке рекурсии встречается
        temp = ''  # встречается почти во всем случаях, кроме значений меньше того что на строке 106
        for i in range(len(s_val) - 1):
            if s_val[i + 1].isdigit():
                temp += s_val[i+1]
                continue
            if not s_val[i].isdigit() and not s_val[i-1].isdigit():
                temp += s_val[i]
        print(temp[1:])
    return s_val


print_exp(build_parse_tree('( ( 10 - 8 ) )'))

