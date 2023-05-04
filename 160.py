#161 ,encoding="UFT-8"
f=open("새파일.txt",'w')
for i in range(1,11):
    data="%d번째 줄입니다.\n"%i
    f.write(data)
f.close()
print("163================")
f=open("새파일.txt",'r')
line=f.readline()
print(line)
f.close()
print("163================")
f=open("새파일.txt",'r')
while True:
    line=f.readline()
    print(line)
    if not line: break
f.close()
