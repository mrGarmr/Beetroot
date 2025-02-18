# Pick your solution to one of the exercises in this module. 
# Design tests for this solution and write tests using unittest library. 

import unittest

class Iterable:
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


class TestIterable(unittest.TestCase):
    '''tests for iterable'''
    def setUp(self):
        self.iterator = Iterable(['a', 4, 1, 'ser', 'ku'])

    def test_for_in_loop(self):
        #Checking if the result equal output

        result = []
        for item in self.iterator:
            result.append(item)
        
        self.assertEqual(result, ['a', 4, 1, 'ser', 'ku'])

    def test_getitem_valid_index(self):
        #Checking index of element
        self.assertEqual(self.iterator[0], 'a')
        self.assertEqual(self.iterator[2], 1)
        self.assertEqual(self.iterator[4], 'ku')

    def test_getitem_invalid_index(self):
        #Indexerror with wrong index
        with self.assertRaises(IndexError):
            self.iterator[5] 

    def test_iteration_work_properly(self):
        # Test if iteration works properly and raises StopIteration
        iterator = iter(self.iterator)
        # ['a', 4, 1, 'ser', 'ku']
        self.assertEqual(next(iterator), 'a')
        self.assertEqual(next(iterator), 4)
        self.assertEqual(next(iterator), 1)
        self.assertEqual(next(iterator), 'ser')
        self.assertEqual(next(iterator), 'ku')
        
        with self.assertRaises(StopIteration):
            next(iterator)


if __name__ == '__main__':
    unittest.main()
