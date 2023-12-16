import random
p1=input("1. ")
p2=input("2. ")
p3=input("3. ")
p4=input("4. ")
p5=input("5. ")
p=[p1,p2,p3,p4,p5]
print("Tun.Hamma uxlasin")
mafia=random.choice(p)
print("Mafia:",mafia)
def f():
 pm=input(mafia+" kim o'yindan chiqadi: ")
 p.remove(pm)
 print(pm,"o'yindan chiqdi")
 sp=", ".join(p)
 print("Qolgan ishtirokchilar:",sp)
 ovoz=input("Mafia kim edi: ")
 if len(p)==2:
   print("Mafia yutdi. Mafia",mafia,"edi")
 elif ovoz==mafia:
  print("O'yin tugadi. Mafia qo'lga tushdi\nMafia:",mafia,"edi")
 else:
  print("Mafia",ovoz,"emas edi. Mafia omon chiqdi.Keyingi tunda ehtiyot bo'lilar")
  f()
f()