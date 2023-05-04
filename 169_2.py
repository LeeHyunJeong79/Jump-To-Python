#점수 텍스트파일sample.txt에 쓰기
f=open("sample.txt",'w')
data=(70,60,55,75,95,90,80,80,85,100)
for i in data:
   f.write(str(i)+'\n')
f.close()

#점수 읽어오기sample.txt
f=open("sample.txt",'r')
sum=0
a=0
avg=0
while True:
    data=f.readline()
    if not data:break
    a+=1
    sum=sum+int(data)
avg=sum/a
f.close()
#평균 기록하기result.txt
f=open("result.txt",'w')
f.write(str(avg))
f.close()

