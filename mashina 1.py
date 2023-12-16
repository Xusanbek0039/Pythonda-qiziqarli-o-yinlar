import time
import random
from itertools import cycle
cars="🚔","🚘","🚖","🚍"
c=random.choice(cars)
nums=0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1
for i in range(10):
 n=random.choice(nums)
 m=[(c+" "+str(n),n)]
 r=cycle(m)
 x,y=next(r)
 print(x)
 time.sleep(y)
print("🏁")