f=open("새파일.txt",'r')
line=f.readlines() #리스트 형태로 반환
print(line)  
f.close()

f=open("새파일.txt",'r')
lines=f.readlines() #리스트 형태로 반환
for line in lines:
    print(line)  #두 줄씩 엔터, 새파일에 \n저장+ print()함수 자체 엔터
f.close()

f=open("새파일.txt",'r')
lines=f.readlines() #리스트 형태로 반환
for line in lines:
    print(line,end="")  #한 줄씩 엔터, 새파일에 \n저장+ print()함수 자체 엔터 안함. 
f.close()

f=open("새파일.txt",'r')
lines=f.readlines() #리스트 형태로 반환
for line in lines:
    print(line.split("\n"))  #두 줄씩 엔터, 새파일에 \n저장+ print()함수 자체 엔터
f.close()