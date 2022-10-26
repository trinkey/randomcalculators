import random
a=int(input())
while a != 0:
 for i in range(a):
  if random.randint(0,1)==1:
   a-=1
 print(a)