'''
Дано - атрибуты и методы присутствующие в классе:
Класс "Задвижка". Атрибуты: состояние (OPEN или CLOSE),
 время открытия-закрытия. Методы: Открыть, Закрыть,
 в обоих случаях выводится предупреждение об операции
 и производится пауза, соответствующая времени операции
  и выводится новое состояние задвижки. Если задвижка уже4 находится в
заданном состоянии выводится сообщение об ошибке.
'''

import time

class Gate:

    def __init__(self, state, closing_time):

        state = state.lower()
        if state in ['open','opened','not_closed']: state = 'OPENED'
        elif state in [ 'close', 'closed', 'not_opened' ]: state = 'CLOSED'
        else: raise ValueError
        self.pause = closing_time
        self.state = state


    def close(self):
        if self.state == 'CLOSED':
            print('The gate is already closed')
        else:
            self.state = 'CLOSED'
            time.sleep(self.pause)
            print('The gate has been closed')

    def open(self):
        if self.state == 'OPEN':
            print('The gate is already opened')
        else:
            self.state = 'CLOSED'
            time.sleep(self.pause)
            print('The gate has been opened')

gate1 = Gate('opened',5 )
gate1.close()
gate1.open()
gate1.open()