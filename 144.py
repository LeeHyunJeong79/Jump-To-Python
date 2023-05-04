#144
def sum(a,b):
    return a+b
print(sum(3,4))

#145
def sum1(a,b):
    print("%d +%d의 합은 %d입니다."%(a,b,a+b))
print(sum1(4,5))

#147
def sum2(*args):
    sum=0
    for i in args:
        sum+=i
    return sum
print(sum2(1,2,3,4,5))

def print_kwargs(**kwargs):
    for k in kwargs.keys():
        if(k=='name'):
            print("당신의 이름은 :" +k)
print(print_kwargs(a='1',name='lee'))