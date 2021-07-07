class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)

        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
    def __iter__(self):
        if self.head:
            current = self.head
            while current:
                yield current.value
                current = current.next
    def __str__(self) -> str:
        result = ""
        current = self.head
        while current:
            result += str(current.value)
        return f"{result} > None"



class HashMap:
    def __init__(self, size=1024):
        self.size=size
        self._bucket = self.size * [None]
    
    def _hash(self, key):
        sum = 0
        for char in key:
            sum += ord(char)
        return sum*19 % self.size


    def __setitem__(self,key,value):

        index = self._hash(key)

        if not self._bucket[index]:
            self._bucket[index] = LinkedList()
          
        current = self._bucket[index].head
        while current:
            if current.value[0] == key:
                current.value[1] = value
                return
            current = current.next
        self._bucket[index].add([key, value])


    def __getitem__(self,key):
        index = self._hash(key) 
        if self._bucket[index]:
            current = self._bucket[index].head
            while current:
                if current.value[0] == key:
                    return current.value[1]
                current = current.next
        # raise KeyError('Key is not found')
        return 'Null'

    def __contains__(self,key):
        index = self._hash(key)
        if self._bucket[index]:
            current = self._bucket[index].head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next
        return False

    def __iter__(self):
        for items in self._bucket:
            if items:
                for item in items:
                    yield item
    
    def __eq__(self, other):
        self.result = []
        for items in self._bucket:
            if items:
                for item in items:
                    self.result += item
        print('inside eq res', self.result)
        print('inside eq oth', other)

        return other == self.result
        
    def __str__(self) -> str:
        result = ''
        for ni in self._bucket:
            if ni:
             for item in ni:
                 result += str(item)
        return result

if __name__ == '__main__':
    test = HashMap()


    test['faisal'] = 'abuzaid'
    test['ayah'] = 'abuhammad'
    test['raad'] = 'abuzaid'
    print(test)
    # for tst in test:
    #     print(tst)
    if test == ['raad', 'abuzaid', 'faisal', 'abuzaid', 'ayah', 'abuhammad']:
        print('it worked')
    