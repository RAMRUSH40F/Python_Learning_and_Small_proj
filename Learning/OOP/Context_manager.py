from contextlib import contextmanager

class Resource:
    def __init__(self,*args):
        self._opened = False
        self.args = args

    def open(self,*args):
        print(f'Resource has been opened with password{args}')
        self._opened = True

    def close(self):
        print(f'The resource was closed')
        self._opened = False

    def __del__(self):
        if self._opened :
            print('The resource was not closed, memory were saved incorrectly')
    @staticmethod
    def imitate_action():
        print('Doing some work')

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self:
            self.close()


if __name__ == '__main__':

    source = Resource(15,15,125, 'g1','gdrive')

    with Resource(1,521) as res:
        res.imitate_action()
        res.imitate_action()
        res.imitate_action()
        raise ValueError('Проверка закрытия соединения')

    # Корявый способ обработать
    # try:
    #     resource = Resource()
    #     resource.open(1,2,4,5, 'g1')
    #     resource.imitate_action()
    #     raise ValueError('Oops')
    #
    # except:
    #     raise
    #
    # finally:
    #     resource.close()

