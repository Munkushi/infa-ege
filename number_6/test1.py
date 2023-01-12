from turtle import *

left(90)
color("black", "red")
m = 10
speed(0)


begin_fill()

for _ in range(10):
    forward(15*m)
    right(90)
    forward(15*m)
    right(90)


end_fill()
canv = getcanvas()

count = 0


for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        item = canv.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1

print(count)
