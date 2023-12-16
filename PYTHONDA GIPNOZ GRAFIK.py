from turtle import*
import colorsys
speed(0)
pensize(2)
h=0.5
bgcolor("black")
for i in range(160):
 c=colorsys.hsv_to_rgb(h,1,1)
 color(c)
 h+=10
 for j in range(2):
  fd(i)
  rt(90)
  rt(15)
 rt(120)
done()