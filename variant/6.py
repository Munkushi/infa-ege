from turtle import *

color("black", "red")
speed("fastest")
left(90)
m = 1

begin_fill()

for _ in range(3):
    forward(10*m)
    right(120)

end_fill()

cv = getcanvas()
count = 0

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        item = cv.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1

print(count)