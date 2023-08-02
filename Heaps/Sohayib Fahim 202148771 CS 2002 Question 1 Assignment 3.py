#
# Name: SOHAYIB SAZID FAHIM
# Student ID: 202148771
#

# COMP 2002 - Assignment 3
# Terrence Tricco
# October 2022


class Heap():

    def __init__(self):
        self._data = [None]
        self._size = 0

    def is_empty(self):
        return self._size == 0


    def insert(self, k):
        """ Adds a new key to the heap. """
        self._size += 1
        self._data.append(k)
        self._upheap(self._size)

    def _upheap(self, c):
        """ Up-heap bubbling after new key insertion. """
        if c > 1:
            p = c // 2
            if self._data[p] > self._data[c]:
                temp = self._data[p]
                self._data[p] = self._data[c]
                self._data[c] = temp
                self._upheap(p)


    def min(self):
        """ Returns, but does not remove, the minimum key stored at the root. """
        if self.is_empty():
            raise IndexError('Heap is empty.')
        return self._data[1]


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
        left = 2 * p
        right = 2 * p + 1
        if left > self._size:  # children exceed array bounds
            return

        # handle special case where a node has left child but not right child
        c = left
        if right <= self._size:
            if self._data[left] > self._data[right]:
                c = right

        if self._data[c] < self._data[p]:
            temp = self._data[p]
            self._data[p] = self._data[c]
            self._data[c] = temp
            self._downheap(c)

    def get_keys(self,depth):
        lst= []
        start = 2**depth
        while start != len(self._data)-1:
            lst.append(self._data[start])
            start +=1

                            # time complixity big O(n)
        return lst



