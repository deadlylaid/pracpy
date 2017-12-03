class Stack:

    def __init__(self):
        self.stack = []

    @property
    def size(self):
        length=0
        for _ in self.stack:
            length+=1
        return length

    def push(self, value):
        self.stack += [value]

    def pop(self):
        length = self.size()

        if length == 0:
            raise IndexError('스택이 비었습니다.')
        else:
            value = self.stack[-1]
            self.stack = self.stack[:length-1]
            return value

    @property
    def top(self):
        length = self.size()
        if length == 0:
            raise IndexError('스택이 비었습니다.')
        else:
            return self.stack[length-1]

    @property
    def is_empty(self):
        length = self.size()
        if length == 0:
            return True
        else:
            return False

    def data_print(self):
        return self.stack

    @property
    def clear(self):
        self.stack = []
