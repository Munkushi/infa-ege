from turtle import *

# Направо 30
# Повтори 60 [Направо 15 Вперёд 3 Направо 45]

left(90)
color("black", "red")
m = 30 # масштаб
right(30)

begin_fill()

for _ in range(6):
    speed(100)
    right(15)
    forward(3*m)
    right(45)

end_fill()

# goto(0, 0)
canvas = getcanvas()
count = 0


for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        item = canvas.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1

print(count)