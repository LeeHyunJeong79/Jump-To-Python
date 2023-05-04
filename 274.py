#구구단
def GuGu(a):
    result=[]
    for i in range(1,10):
        result.append(a*i)
    return result
print(GuGu(2))