'''На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO. 
Объяснить плюсы и минусы каждой реализации.
Первый класс - простое представление работы метода deque модуля collections. Совершает как операцию append за O(1), так и операцию popleft.
Второй класс - примитивный вид циклического буфера. append в этом случае совершается за O(1), а pop за O(n) (n - количество элементов в массиве, 
так как ему необходимо будет "сдвигать" элементы влево).
P.S. Учился с версии 3.x, не уверен, что все верно написано для версии 2.7
'''

import collections


# Аргумент класса - максимальное количество элементов в массиве
class CircularBuffer_1(object):
    def __init__(self, maximum_el = 5):
        self.q = collections.deque(maxlen = maximum_el)
    
    def append(self, item):
        self.q.append(item)
        return self.q
    
    def pop(self):
        self.q.popleft()
        return self.q
    
    def prnt(self):
        print self.q
      

class CircularBuffer_2(object):
    def __init__(self, data = [], maximum_el=5):
        self.data = data
        self.max = max_size
        
    def append(self, item):
        if len(self.data) < self.max:
            self.data.append(item)
            print self.data
            return self.data
        else:
            self.data.pop(0)
            self.data.append(item)
            print self.data
            return self.data
    
    def pop(self):
        self.data.pop(0)
        return self.data
    
    def prnt(self):
        print self.data

