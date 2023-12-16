import time
from itertools import cycle
chiroqlar =[
("🔴",3),
("🟡", 1.5),
("🟢", 3),
("",0)
]
ranglar = cycle(chiroqlar)
while True:
 c,s= next(ranglar)
 print(c)
 time.sleep(s)