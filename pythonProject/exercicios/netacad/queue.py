class QueueError(IndexError):
    pass

class Queue:
    def __init__(self):
        self.__fifo = []


    def put(self, elem):
        self.__fifo.append(elem)


    def get(self):
        if len(self.__fifo) > 0:
            elem = self.__fifo[0]
            del self.__fifo[0]
            return elem
        else:
            return QueueError





que = Queue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    print(que.get())