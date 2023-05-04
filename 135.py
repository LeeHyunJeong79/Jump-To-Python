#135
for i in range(2,10):
    for j in range(1,10):
        print("%d*%d=%d"%(i,j,i*j),end=" ")
    print('')

#136  a*3
a=[1,2,3,4]
result=[]
for num in a:
    result.append(num*3)
    if num%2==0 :
        result.append(num*3)
print(result)

#136 a중 짝수만 *3
a=[1,2,3,4]
result=[]
for num in a:
    if num%2==0 :
        result.append(num*3)
print(result)

#137 리스트 내포
result=[x*y for x in range(2,10) for y in range(1,10) ]
print(result)