import random, time
from itertools import cycle
def  bekat(r):
 y_t=random.randint(15,200)
 y_ch=random.randint(15,200)
 km=random.randint(5,10)
 vagon=[("🚇",0.1)]
 vc=cycle(vagon)
 x,y=next(vc)
 for i in range(km):
  print(x)
  time.sleep(y)
 print("Bekat",r)
 print(y_t,"yulovchi tushdi➡️\n"+str(y_ch)+" yulovchi chiqdi⬅️\n🏃🏃‍♂🏃‍♂\n⏳")
 time.sleep(3)
 bekat(r+1)
bekat(1)