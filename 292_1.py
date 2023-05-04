def string_count(data):
    cc=""
    result=0 #문자의 수
    c_result="" #출력결과 
    for c in data:
        if c==cc:
            result+=1 #문자개수더하기
        else:
            cc=c
            if result :
                c_result=c_result+str(result) #출력결과에 문자수 추가 
            result=1   #문자개수 초기화 
            c_result+=c #출력결과에 문자 추가 
    c_result=c_result+str(result) #마지막 문자의 문자수 추가 
 
    return c_result
        
 
data=input()
print(string_count(data))
