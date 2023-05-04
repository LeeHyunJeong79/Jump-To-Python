#1
a=(1,2,3)
a=a+(4,)
print(a)

#2
a={'A':90,'B':80,'C':70}
result= a.pop('B')
print(a)
print(result)

#3
a=[1,1,1,2,2,3,3,3,4,4,5]
aset=set(a)
b=list(aset)
print(aset)

#4
a=b=[1,2,3]
a[1]=4
print(a)
print(b)

