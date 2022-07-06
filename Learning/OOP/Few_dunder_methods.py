from queue import Queue as queue_base
import inspect
# print(inspect.getsource(queue_base))


class Queue(queue_base):
    #Asks for string version of an object
    def __repr__(self):
        return f'Queue object({self._qsize()})'

    # Put a new item in the queue
    def __add__(self, other):
        self.put(other)

    def __call__(self, *args, **kwargs):
        self.put(args)

if __name__ == '__main__':
    qu1 = queue_base()
    qu2 = Queue()

    print(qu2)
    qu2+8
    print(qu2)
    qu2(6)
    print(qu2)