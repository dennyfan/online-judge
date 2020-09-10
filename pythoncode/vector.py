#!/usr/bin/env python3
import operator as op
class vector:
    def __init__(self, *v):
        self._v = list(v)
    def __repr__(self):
        return __class__.__name__ + repr(tuple(self._v))
    def __add__(self, right):
        return vector(*map(op.add, self._v, right._v))
    def __iadd__(self, right):
        self._v[:] = map(op.add, self._v, right._v)
    def __sub__(self, right):
        return vector(*map(op.sub, self._v, right._v))
    
    def __len__(self):
        return len(self._v)
    def __getitem__(self, i):#__getitem__(2),或(slice(2,5))
        if type(i) == int:
            return self._v[i]
        elif type(i) == slice:#ex.即i為2:5（=slice(2,5))
            return vector(*self._v[i])#()
        else: raise TypeError(type(i).__name + 'unsupported')
    def __setitem__(self, i, v):
        if type(i) == int:
            self._v[i] = v#so if z[0] = 1,2，結果會是vector((1,2),2,3.....)
        elif type(i) == slice:
            self._v[i] = v._v if isinstance(v, vector) else v#so if z[0:2]=y,結果會是vector(4,5,6,3,4,5,6,7,8),and actually v._v[:] is correct
        else: raise TypeError(type(i).__name + 'unsupported')#if z[:4]=1,2,結果會是vector(1,2,5,6,7,8)
    #z = vector(*range(1,9))
    #y = vector(4,5,6)