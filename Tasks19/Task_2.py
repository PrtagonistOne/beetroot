from sys import path
import Task_1 # не баче
print(path)
path[0] = '/home/protagonist/Beetroot/Module_1/Tasks17'  # змінив початкову корньову папку
print(path)
import Task_1  # зміна шляху sys.path впливає на пошук модулів
