#131
marks=[90,25,67,45,80]
number=0
for mark in marks:
    number+=1
    if mark>=60:
        print("%d번 학생은 %d점 합격입니다." %(number,mark))
    else:
        print("%d번 학생은 %d점 불합격입니다."  %(number,mark))
print("================================")
#132
for mark in marks:
    number+=1
    if mark>=60:
        continue
    print("%d번 학생은 %d점 합격입니다."  %(number,mark))
print("================================")

#134
sum=0
for i in range(1,11):
    print(i)
    sum+=i
print("합계=%d"%sum)
