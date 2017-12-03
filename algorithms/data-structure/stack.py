class Stack(object):

    def __init__(self, limit=10):
        self.stack = []
        self.limit = limit

    def __bool__(self):
        return not bool(self.stack)

    def __str__(self):
        return str(self.stack)

    def push(self, value):
        if len(self.stack) >= self.limit:
            raise StackOverFlowError('정해진 길이를 초과함')
        self.stack.append(value)

    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            raise IndexError('데이터가 존재하지 않음')

    def size(self):
        return len(self.stack)

class StackOverFlowError(BaseException):
    pass
