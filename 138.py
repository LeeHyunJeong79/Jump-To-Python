#1
a="Life is too short, you need python"
if "wife" in a and "you" not in a:print("phyhon")
elif "shirt" not in a:print("shirt")
elif "need" in a:print("need")
else: print("none")

#2
i=0
while True:
    i+=1
    if i>5 : break
    print('*'*i)

#3
a=[70,60,55,75,95,90,80,80,85,100]
total=0
for i in a:
    total+=i
average=total/len(a)
print(total,average)
