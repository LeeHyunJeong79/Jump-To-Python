class HousePark():
    lastname="박"
    def __init__(self,name):
        self.name=self.lastname+name
    def travel(self,where):
        print("%s,%s여행을 가다."%(self.name,where))
    def love(self,other):
        print("%s,%s 사랑에 빠졌네"%(self.name,other.name))
    def __add__(self,other):
        print("%s,%s 결혼했네"%(self.name,other.name))

class HouseKim(HousePark):
    lastname="김"
    def travel(self,where,day): #메서드 오버라이딩
        print("%s,%s여행 %d일 가네."%(self.name,where,day))

pey=HousePark("응용")
pey.travel("태국")
pey2=HouseKim("줄리엣")
pey2.travel("독도",3)
pey.love(pey2)
pey2.love(pey)
pey+pey2 #__add__()함수 호출
