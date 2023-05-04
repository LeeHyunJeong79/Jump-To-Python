class FourCal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result=self.first/self.second
        return result
a=FourCal(2,9)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
#상속
class MoreFourCal(FourCal):
    def pow(self):
        result=self.first**self.second
        return result
class safeFourCal(FourCal):
    def div(self):
        if self.second==0 :
            return 0
        else :
            return self.first/self.second


a=MoreFourCal(3,4)
b=safeFourCal(5,0) #메서드 오버라이딩 
print("상속=" ,a.add())
print("오버라이딩=",b.div())