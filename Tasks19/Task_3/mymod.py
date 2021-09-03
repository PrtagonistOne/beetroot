import sys


def count_lines(name: str) -> str:
    value = str(len(open(name, 'r').readlines()))
    return value


def count_chars(name: str) -> str:
    f = str(len(open(name, 'r').read()))
    return f


def very_ambitions_func(name: str) -> str:
    f = open(name, 'r')
    num_of_lines = str(len(f.readlines()))
    f.seek(0)
    num_of_chars = str(len(f.read()))
    return num_of_lines + ' ' + num_of_chars

def test(name: str):
    a = count_chars(name)
    b = count_lines(name)
    return b + ' ' + a


print(sys.path[0])
print(count_lines('text.txt'), count_chars('text.txt'))
sys.path[0] = "/home/protagonist/Beetroot/Module_1/Tasks19/Task_1"
print(test('text.txt'))
print(sys.path[0])

# PYTHONPATH DOES NOT need to include the directory where you created mymod.py

print(very_ambitions_func('text.txt'))