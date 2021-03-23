a = []
first, last = -1, -1
size = 5


def push(value):
    isFull()
    a.append(value)
    global last
    last += 1


def pop():
    global first
    first += 1
    return a[first]


def isFull():
    if len(a) == size:
        return BufferError



push(1)
push(2)
push(3)
push(4)
push(5)
push(6)
print(a)
print(pop())
print(pop())
print(a)

