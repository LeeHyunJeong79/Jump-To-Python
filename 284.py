import sys
filename=sys.argv[0]
src=sys.argv[1]
dst=sys.argv[2]
f1=open(src,'r')
tab_content=f1.read()

space_content=tab_content.replace('\t'," ")
f2=open(dst,'w')
f2.write(space_content)
print(tab_content)

f1.close()
