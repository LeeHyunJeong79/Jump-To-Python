def check_Num(s):
    result=""
    for n in s:
        if n not in result:
            result+=str(n)
        else:
            return "false"
    if len(result)==10:
        return "true"
    else : return "false"
data=str(input()) #숫자입력 

for i in data.split(): #띄어쓰기를 기준으로 숫자를 자른 후 함수 호출 
   print(check_Num(i),end=" ")