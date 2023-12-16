import random, time
from itertools import cycle
cars="🚖","🚘","🚍","🚔"
speed=0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1
p1=input("Birinchi o'yinchi: ")
p2=input("Ikkinchi o'yinchi: ")
f="🏁"
c1=random.choice(cars)
c2=random.choice(cars)
t1=0
print(p1)
for i in range(10):
 s1=random.choice(speed)
 m=[(c1+" "+str(s1),s1)]
 r=cycle(m)
 x,y=next(r)
 print(x)
 time.sleep(y)
 t1=t1+s1
print(f+"\n"+"Tezlik: "+str(t1)+" sekund")
print(p2)
t2=0
for i in range(10):
 s2=random.choice(speed)
 m=[(c2+" "+str(s2),s2)]
 r=cycle(m)
 x,y=next(r)
 print(x)
 time.sleep(y)
 t2=t2+s2
print(f+"\n"+"Tezlik: "+str(t2)+" sekund")
if t1<t2:
 print(p1,"yutdi")
elif t1>t2:
 print(p2,"yutdi")
else:
 print("Durrang")