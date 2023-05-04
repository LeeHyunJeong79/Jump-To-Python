f=open("새파일.txt",'r')


lines=f.readlines()
print(lines)
f=open("새파일.txt",'r')
data=f.read() #파일의 내용 전체를 문자열로 리턴
print(data)

f.close()