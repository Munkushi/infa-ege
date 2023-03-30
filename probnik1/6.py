from turtle import *

# Направо 45
# Повтори 10 [Вперёд 2 Направо 36]

left(90)
speed(10)
color("black", "red")
m = 10
right(45)

begin_fill()


for _ in range(18):
    forward(18*m)
    right(90)
forward(18*m)

for z in range(18):
    left(90)
    forward(18*m)

end_fill()
canv = getcanvas()

count = 0


for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        item = canv.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1

print(count)
