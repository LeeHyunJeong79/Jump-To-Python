#118
pocket=['paper','cellphone']
card=1
if 'money' in pocket:
     print("타고가기")
elif card:
     print("카드로 타고가기")
elif 'cellphone' in pocket:
    print("전화기로 타고가기")
else:
    print("걸어가라")

#if 정규표현식
score=70
if score>=60:
    message="sucess"
else:
    message="failure"
print(message)

message="sucess" if score>-60 else "failuse"
print(message)
