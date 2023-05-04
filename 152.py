#154
a=1
def vartest(a):
    a=a+1
vartest(a)
print(a)

#156
a=1
def vartest():
    global a
    a=a+1
vartest()
print(a)

#함수정의 lambda함수 사용..주석부분과 동일기능 수행
#def add(a,b):
#   return a+b

add=lambda a,b:a+b
print(add(1,2))

#lambd함수 활용
mylist=[lambda a,b:a+b, lambda a,b:a*b]
print(mylist[0](1,2))
print(mylist[1](2,2))
print(mylist[0](1,2),mylist[1](1,2))