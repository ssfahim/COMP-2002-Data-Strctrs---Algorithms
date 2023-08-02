#
# Name: SOHAYIB SAZID FAHIM
# Student ID: 202148771
#

# COMP 2002 - Assignment 3
# Terrence Tricco
# October 2022

class TernaryHeap():
    
    def __init__(self):
        self._data = [None]
        self._size = 0

    def is_empty(self):
        return self._size == 0

    def insert(self, k):
        self._size += 1
        self._data.append(k)
        self._upheap(self._size)

    def _upheap(self, c):
        if c > 1:
            p = (c + 1) // 3
            if self._data[p] > self._data[c]:
                temp = self._data[p]
                self._data[p] = self._data[c]
                self._data[c] = temp
                self._upheap(p)

    def remove_min(self):
        """ Remove and return the minimum key stored at the root. """
        if self.is_empty():
            raise IndexError('Heap is empty.')
        e = self._data[1]
        self._data[1] = self._data[self._size]
        self._data.pop()
        self._size -= 1
        self._downheap(1)
        return e

    def _downheap(self, p):
        """ Down-heap bubbling after removal. """
        left =  3 * p - 1
        middle = 3 * p
        right = 3 * p + 1
        if left > self._size:  # children exceed array bounds
            return

        c = left

        if middle < self._size:
            if self._data[left] > self._data[middle]:
                c = middle

        if right <= self._size:
            if  self._data[middle] > self._data[right]:
                c = right

        if self._data[c] < self._data[p]:
            temp = self._data[p]
            self._data[p] = self._data[c]
            self._data[c] = temp
            self._downheap(c)

