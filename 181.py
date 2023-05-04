class Service:
    secret="영구는 배꼽이 두개다."
    def setname(self,name):
        self.name=name
    def sum(self,a,b):
        result=a+b
        print("%s님 %s+%s=%s입니다."%(self.name,a,b,result))
pey=Service()
pey.setname("홍길동") #이 문장이 없을 경우 error발생
pey.sum(3,4)
