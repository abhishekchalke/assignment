


class Rectangle():
    '''Rectangle class, which takes length and width as parameters'''
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __iter__(self):
        self._index = 0
        return self


    def __next__(self):
        if self._index == 0:
            self._index += 1
            return {'length':self.length}
        elif self._index == 1:
            self._index += 1
            return {'width':self.width}
        else:
            raise StopIteration



rectangle = Rectangle(length=8, width=3)

for attribute in rectangle:
    print(attribute)




