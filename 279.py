def getTotalPage(m,n):
    if m/n==0:
        return m/n

    else:
        return m//n+1
print(getTotalPage(5,10))
print(getTotalPage(15,10))
print(getTotalPage(20,10))
print(getTotalPage(25,10))
print(5/10) #소수점까지 출력
print(5//10) #몫만 출력
