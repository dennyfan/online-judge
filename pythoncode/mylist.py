#!/usr/bin/env python3
class mylist(list):
    def __repr__(self):
        return self.__class__.__name__ + '('+super().__repr__()+')'
    def find(self, val):
        def recfind(l, val):
            if isinstance(l, list) or isinstance(l, tuple):
                for i, v in enumerate(l):
                    p = recfind(v, val)
                    if p == True:
                        return (i, )
                    if p != False:
                        return (i, ) + p
            return l == val
        return recfind(self, val)

    def sort(self, key=None, reverse=False):
        D = {'NoneType':0, 'int':1, 'float':1, 'str':2, 'tuple':3, 'list':4}
        return super().sort(key= lambda x: (D.get(type(x).__name__, 5), key(x) if key is not None else x)\
                            , reverse= reverse)

    #if __name__ == '__main__':
    #M = mylist([3, 8, 'hello', 7.4, ('world', 15), [4, 7],'Hello'])
    #N = mylist([7.4, 2,'world','bye', (13,	24), 'bye', (14, 28), None])
class mysublist(mylist):# question
    def __repr__(self):
        return self.__class__.__name__ + '('+super(mylist, self).__repr__()+')'
