import operator
from typing import Generic, TypeVar, List

from oop_tree import BinaryTree

T = TypeVar("T")


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
    stack = Stack()
    tree: BinaryTree = BinaryTree('')
    stack.push(tree)
    current_tree = tree

    temp_nums = math_exp
    temp_signs = math_exp
    temp = []

    signs = ['+', '-', '*', '/', ')', '(']
    nums = list(range(10))
    for i in signs:
        temp_nums = temp_nums.replace(i, ' ')
    for i in nums:
        temp_signs = temp_signs.replace(str(i), ' ')

    for i in range(len(temp_signs.split())):
        temp.append(temp_signs.split()[i])
        if i < len(temp_nums.split()):
            temp.append(temp_nums.split()[i])

    s = ' '.join(temp)

    temp_signs1 = []
    for i in s.split():
        if len(i) > 1 and not i.isdigit():
            for j in range(0, len(i)):
                temp_signs1.append(i[j])
        else:
            temp_signs1.append(i)

    for i in temp_signs1:

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


def print_exp(tree: BinaryTree, inner = 1) -> str:
    s_val = ""
    if tree:
        s_val = '(' + print_exp(tree.get_left_child())
        s_val = s_val + str(tree.get_root_val())
        s_val = s_val + print_exp(tree.get_right_child())+')'

    return s_val


print(evaluate(build_parse_tree('((10-8)*20)')))
