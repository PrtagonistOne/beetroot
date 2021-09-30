import timeit
from random import shuffle


def timer(function):
    def new_function(array):
        start_time = timeit.default_timer()
        function(array)
        elapsed = timeit.default_timer() - start_time
        print('Function "{name}" took {time} seconds to complete.'.format(name=function.__name__, time=elapsed))

    return new_function


@timer
def bubble_sort_both_directions(array):
    n = len(array)
    swapped = True
    start = 0
    end = n - 1
    while swapped:
        swapped = False
        for i in range(start, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        if not swapped:  # якщо нічого не було свапнуто, значить масив відсортовано
            break
        swapped = False
        end -= 1

        for i in range(end - 1, start - 1, -1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
        start += 1


@timer
def bubble_sort(array):
    for pass_num in range(len(array) - 1, 0, -1):
        for i in range(pass_num):
            if array[i] > array[i + 1]:
                temp = array[i]
                array[i] = array[i + 1]
                array[i + 1] = temp


a = list(range(50))
b = a
shuffle(a)
b = a.copy()
bubble_sort_both_directions(a)  # також відоме як сортування коктейлем, трохи швидше бульбашкою
bubble_sort(b)  # звичайне сортування бульбашкою трохи повільніше
