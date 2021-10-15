import time
from multiprocessing import Queue

colors = ['red', 'green', 'blue', 'black']

cnt = 1
queue = Queue()
print('pushing items to queue')
for color in colors:
    print(f"item #{cnt} - {color}")
    queue.put(color)
    cnt += 1

print('\npopping items from queue: ')
cnt = 0
while not queue.empty():
    print(f"item #{cnt} - {queue.get()}")
    cnt += 1
# def print_func(continent = "Asia"):
#     print('The name of continent is: ', continent)
#
# if __name__ == "__main__":
#     names = ['America', 'Europe', 'Africa']
#     procs = []
#     # proc = Process(target=print_func)
#     # procs.append(proc)
#     # proc.start()
#
#     for name in names:
#         proc = Process(target=print_func, args=(name,))
#         procs.append(proc)
#         proc.start()
#         time.sleep(5)
#         print(procs)
#
#     for proc in procs:
#         proc.join()