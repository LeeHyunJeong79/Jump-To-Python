#126
coffee=10
money=300
while money:
    print("돈을 받았습니다. 커피 %d회 제공합니다" %coffee)
    coffee=coffee-1
    if not coffee:
        print("커피가 다 떨어졌습니다.판매를 중지합니다")
        break
    
#128
a=0
while a<10:
    a=a+1
    if a%2==0:
        continue
    print(a)