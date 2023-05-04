a=[1,2,3]
b=a
a[1]=4
print(a)
print(b)
print(a is b)

from copy import copy
a=[1,2,3]
b=copy(a)
a[1]=4
print(a)
print(b)
print(a is b)

a=[1,2,3]
b=a[:]
a[1]=4
print(a)
print(b)
print(a is b)
#http://pythontutor.com/visualize.html#mode=display 코드 확인