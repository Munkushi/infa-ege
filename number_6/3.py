from turtle import *

# Направо 45
# Повтори 10 [Вперёд 2 Направо 36]

left(90)
color("black", "red")
m = 30
right(60)

begin_fill()


for _ in range(12):
    left(15)
    forward(3*m)
    left(15)


end_fill()
canv = getcanvas()

count = 0


for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        item = canv.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1

print(count)
