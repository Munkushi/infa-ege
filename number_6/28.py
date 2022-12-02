from turtle import *

# Повтори 4 [Вперёд 12 Направо 90]
# Направо 30
# Повтори 3 [Вперёд 8 Направо 60 Вперёд 8 Направо 120]

left(90)
color("black", "red")
m = 15
right(60)

begin_fill()


for _ in range(4):
    forward(12*m)
    right(90)


right(30)

for m in range(3):
    forward(8*m)
    right(60)
    forward(8*m)
    right(120)


end_fill()


canv = getcanvas()
count = 0

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        item = canv.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1

print(count)
