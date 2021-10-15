import threading

x = 0

class Counter(threading.Thread):

    def __init__(self, y=100000):
        threading.Thread.__init__(self)
        self.y = y

    def run(self):
        global x
        for i in range(self.y):
            x += 1
        print(x)


thread1 = Counter()
thread1.start()
thread2 = Counter()
thread2.start()
