#문제1
class Calculator:
    def __init__(self,data):
        self.data=data
    def sum(self):
        result=0
        for i in self.data:
            result+=i
        return result
    def avg(self):
        return self.sum()/len(self.data)

cal1=Calculator([1,2,3,4,5])
print(cal1.sum())#합계
print(cal1.avg())#평균
cal2=Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())

