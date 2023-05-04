class FourCal:
    def setdata(self,first,second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
a=FourCal()
a.setdata(5,8)
print(a.first,a.second)
print(a.add())

#상속
class MoreFourCal(FourCal):
    pass
b=MoreFourCal()
b.setdata(3,4)
print("상속=" ,a.add())
