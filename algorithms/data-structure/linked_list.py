class LinkedList:

    class _Node:

        def __init__(self, element, next=None):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0
        self._tail = None

    def add_first(self, value):
        node = self._Node(value)
        if self._size == 0:
            self._head = node
            self._tail = node
            self._size = 1
        else:
            node._next = self._head
            self._head = node
            self._size += 1

    def add_last(self, value):
        node = self._Node(value)
        if self._size == 0:
            self._head = node
            self._tail = node
            self._size = 1
        else:
            self._tail = node
            self._size += 1

#    def add_middle(self, index, value):

    def print_list(self):
        probe = self._head
        while probe is not self._tail:
            print(probe._element, '-> ', end='')
            probe = probe._next
        print(probe._element)
