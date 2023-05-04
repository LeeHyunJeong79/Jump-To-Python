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
    def fight(self,other):
        print("%s,%s 싸우네"%(self.name,other.name))
    def __sub__(self,other):
        print("%s, %s 이혼했네"%(self.name,other.name))
class HouseKim(HousePark):
    lastname="김"
    def travel(self,where,day): #메서드 오버라이딩
        print("%s,%s여행 %d일 가네."%(self.name,where,day))
pey=HousePark("응용")
pey2=HouseKim("줄리엣")
pey.travel("부산")
pey2.travel("부산",3)
pey.love(pey2)
pey2+pey
pey.fight(pey2)
pey-pey2
pey+pey2 #__add__()함수 호출
