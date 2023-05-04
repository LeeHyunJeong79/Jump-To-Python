class FourCal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
a=FourCal(5,8)
print(a.first,a.second)
print(a.add())

#상속
class MoreFourCal(FourCal):
    pass
b=MoreFourCal(3,4)

print("상속=" ,a.add())