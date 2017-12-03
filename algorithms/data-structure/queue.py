class Queue:

    def __init__(self):
        self.queue = []

    def size(self):
        length = 0
        for _ in self.queue:
            length+=1
        return length

    def enqueue(self, value):
        self.queue += [value]

    def dequeue(self):
        if self.size() == 0:
            return IndexError('큐에 아무런 데이터도 존재 하지 않습니다')
        value = self.queue[0]
        self.queue = self.queue[1:]
        return value

    def is_empty(self):
        if self.size() == 0:
            return True
        return False

    def first(self):
        return self.queue[0]

    def top(self):
        return self.queue[-1]

from IPython import embed ;embed()
