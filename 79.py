t1=(1,2)
t2=t1*3
print(t2)
a={1:'a'}
a[2]="b"
print(a)
a={1:'파랑구름', 2:'이현준', 3:"이현정"}
for v in a.items():
    print(v)
for k,v in a.items():
    print("키는: "+str(k))
    print("벨류는"+v)
a=()   #빈 값
b=(1,2,3) #숫자
c=1,2,3 
d=(1, 2, 'life', 'is') #숫자+문자
e=(1, 2, ('life', 'is') ) #숫자+리스트