#메모장 만들기(280p)
import sys
option=sys.argv[1]

if option=='a':
    memo=sys.argv[2]
    fopen=open('memo.txt','a')
    fopen.write(memo)
    fopen.write('\n')
    fopen.close
elif option=='r':
    fopen=open('memo.txt','r')
    line=fopen.readlines()
    print(line)
    fopen.close
