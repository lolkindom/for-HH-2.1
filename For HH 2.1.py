class ListIsEmptyError(Exception):
    pass


class ListIsFullError(Exception):
    pass


class Fifo:
    def __init__(self, limit=5):
        self.head, self.tail = -1, -1
        self.count = 0
        self.limit = limit
        self.circle = [None]*self.limit

    def is_full(self):
        return self.count == self.limit

    def is_empty(self):
        return self.count == 0

    def pop(self):
        if self.is_empty():
            raise ListIsEmptyError
        buff = self.circle[self.head]
        if self.head == self.tail:
            self.head, self.tail = -1, -1
        else:
            self.count -= 1
            self.head = (self.head + 1) % self.limit
        return buff

    def push(self, a):
        if self.is_full():
            raise ListIsFullError
        if self.is_empty():
            self.head += 1
            self.tail += 1
            self.count += 1
            self.circle[self.head] = a
        else:
            self.count += 1
            self.tail = (self.tail + 1) % self.limit
            self.circle[self.tail] = a


if __name__ == '__main__':
    a = Fifo(3)
    a.push(1)
    a.push(2)
    a.push(3)
    assert a.pop() == 1
    a.push(4)
    assert a.pop() == 2



