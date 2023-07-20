#  SOHAYIB SAZID FAHIM
#  202148771

from linked_stack import LinkedStack
class AlphaStack(LinkedStack):
    long = []
    alphalist = []
    counter = 0
    d = {}
    def __int__(self):
        super().__init__()
        self.long = []
        self.alphalist = []
        self.counter = 0

    def push(self, e):
        self._head = self._Node(e, self._head)  # create and link a new node
        self._size += 1
        if len(AlphaStack.long) == 0:
            AlphaStack.long.append(e)
        elif len(AlphaStack.long[0]) == len(e):
            AlphaStack.long.append(e)
        elif len(AlphaStack.long[0])< len(e):
            AlphaStack.long.clear()
            AlphaStack.long.append(e)

        AlphaStack.counter += len(e)


        for c in e:
            if c in AlphaStack.d:
                AlphaStack.d[c] += 1
            else:
                AlphaStack.d[c] = 1

        #for i in range(0, len(AlphaStack.d)):
            #if AlphaStack.d.get(0) == AlphaStack.d.get(i+1):
        AlphaStack.alphalist.append(max(AlphaStack.d, key= AlphaStack.d.get))

    def pop(self):
        if self.is_empty():
            raise IndexError('Stack is empty')
        answer = self._head._element
        self._head = self._head._next  # bypass the former top node
        self._size -= 1
        #if len(answer) == len(AlphaStack.long[0]):
        return answer

    def longest_word(self):
        if len(AlphaStack.long)==1:
            return str(AlphaStack.long[0])
        elif len(AlphaStack.long)>1:
            return AlphaStack.long
        else:
            return None

    def total_characters(self):
        return AlphaStack.counter

    def character_counts(self):
        return AlphaStack.d

    def most_common_character(self):
        return [*set(AlphaStack.alphalist)] # Got this code from here (https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/)



