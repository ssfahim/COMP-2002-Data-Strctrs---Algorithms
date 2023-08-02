#
# Name: SOHAYIB SAZID FAHIM
# Student ID: 202148771
#

# COMP 2002 - Assignment 3
# Terrence Tricco
# October 2022

class OrderedHeap():
    
    def __init__(self):
        self._data = [None]
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def insert(self,k):
        self._size += 1
        self._data.append(k)
        self._upheap(self._size)



    def _upheap(self, c):
        if c > 1:
            p = c // 2
            left = 2 * p
            right = 2 * p + 1
            if right > self._size:
                return

            if right <= self._size:

                if self._data[right] > self._data[left]:
                    temp = self._data[right]
                    self._data[right] = self._data[left]
                    self._data[left] = temp
                if self._data[p] > self._data[c]:
                    temp = self._data[p]
                    self._data[p] = self._data[c]
                    self._data[c] = temp
                self._upheap(p)

    def remove_min(self):
        if self.is_empty():
            raise IndexError('Heap is empty.')
        e = self._data[1]
        self._data[1] = self._data[self._size]
        self._data.pop()
        self._size -= 1
        self._downheap(1)
        return e

    def _downheap(self, p):
        left = 2 * p
        right = 2 * p + 1

        if right > self._size:
            return
        c = right
        if right <= self._size:
            if self._data[left] > self._data[right]:
                c = left
            if self._data[right] > self._data[left]:
                temp1 = self._data[right]
                self._data[right] = self._data[left]
                self._data[left] = temp1

        if self._data[p] > self._data[c]:
            temp = self._data[p]
            self._data[p] = self._data[c]
            self._data[c] = temp
            self._downheap(c)
