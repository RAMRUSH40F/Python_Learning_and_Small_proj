class MoneyBox:
    def __init__(self, capacity):
        self.cap = capacity

    def can_add(self, c):
        if c <= self.cap:
            return True
        else:
            return False

    def add(self, c):
        if self.can_add(c):
            self.cap -= c
        return self.cap
#-----------------------
class Buffer:
    def __init__(self):
        self.nums = list();

    def add(self,*args):

        for i in range (0,len(args)):
            self.nums.append(args[i])
            if len(self.nums)>=5 :

                sum = 0;
                for i in range (0,5):
                    sum +=self.nums[i]
                del self.nums[0:5]

                print(sum)



    def get_current_part(self):
        return self.nums


buf = Buffer()
buf.add(1, 2, 3)
print(buf.get_current_part()) # вернуть [1, 2, 3])
buf.add(4, 5) # print(15) – вывод суммы первой пятерки элементов
print(buf.get_current_part())
