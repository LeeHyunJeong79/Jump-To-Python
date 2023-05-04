f=open("새파일.txt",'r')
lines=f.readlines() #리스트 형태로 반환
print(lines)
for line in lines:
    print(line)  #두 줄씩 엔터, 새파일에 \n저장+ print()함수 자체 엔터
f.close()