# Create your own implementation of an iterable, which could be used inside for-in loop. 
# Also, add logic for retrieving elements using square brackets syntax.

class Iterable:
    '''Own implementation of an iterable, which could be used inside for-in loop'''
    def __init__(self, data):
        self.data = data
        self.index = 0  

    def __iter__(self):
        return self 

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration  

    def __getitem__(self, index):
        if index < len(self.data):
            return self.data[index]
        else:
            raise IndexError("Index out of range")

iterator = Iterable([1, 2, 0, 20, 7])

for i in iterator:
    print(i)

print(20*'_')
print(iterator[3])