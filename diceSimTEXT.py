import random
m,p,r=int(input("rolls -")),[],int(input("sides -"))
for i in range(m):
 p.append(random.randint(1,r))
for i in range(1,r+1):
 print(str(i)+"-"+str(p.count(i)))