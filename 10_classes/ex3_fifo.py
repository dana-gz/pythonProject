class Queue:
    """Implement FIFO"""

    def __init__(self, queue_list):
        self.queue_list = queue_list

    def show(self):
        print(self.queue_list)

    def is_empty(self):
        return len(self.queue_list) == 0

    def put(self, item):
        self.queue_list.append(item)
        print('Item added!')

    def get_fifo(self):
        try:
            return self.queue_list.pop(0)
        except IndexError:
            print('No more elements!')

    def get_lifo(self):
        try:
            return self.queue_list.pop(-1)
        except IndexError:
            print('NO more elements!')


if __name__ == "__main__":
    queue_list = [1, 2, 3]

    fifo = Queue(queue_list)
    fifo.show()
    print(fifo.is_empty())
    item = fifo.get_fifo()
    print(item)

    lifo = Queue(queue_list)
    lifo.show()
    print(lifo.is_empty())
    item = lifo.get_lifo()
    print(item)

    lifo.show()
    print(lifo.is_empty())
    lifo.put('4')
    lifo.put('5')
    lifo.put('6')
    lifo.show()
    item = lifo.get_lifo()
    print(item)
    item = fifo.get_fifo()
    print(item)
    fifo.show()