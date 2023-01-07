from turtle import *

left(90)
m = 30
color("black", "red")

speed(100)

begin_fill()
for _ in range(18):
    forward(42*m)
    right(72)


end_fill()

cv = getcanvas()
count = 0

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        item = cv.find_overlapping(x, y, x,y)
        if len(item) == 0 or item[0] == 5:
            count += 1


print(count)