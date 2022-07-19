'''На языке Python (2.7) реализовать минимум по 2 класса реализовывающих циклический буфер FIFO. 
Объяснить плюсы и минусы каждой реализации.
Первый класс - простое представление работы метода deque модуля collections. Совершает как операцию append за O(1), так и операцию popleft.
Второй класс - примитивный вид циклического буфера. append в этом случае совершается за O(1), а pop за O(n) (n - количество элементов в массиве, 
так как ему необходимо будет "сдвигать" элементы влево.
'''


import collections


# Аргумент класса - максимальное количество элементов в массиве
class CircularBuffer_1(object):
    def __init__(self, maximum_el = 5):
        self.q = collections.deque(maxlen = maximum_el)
    
    def app(self, item):
        self.q.append(item)
        return self.q
    
    def pop(self):
        self.q.popleft()
        return self.q
    
    def pr(self):
        return self.q
      

