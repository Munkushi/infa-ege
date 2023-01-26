from turtle import *

# left(90)
m = 30
color("black", "red")
begin_fill()

for i in range(4):
    forward(9*m)
    right(90)
    forward(3*m)
    right(90)

end_fill()

count = 0
cv = getcanvas()

for x in range(-100*m, 100*m, m):
    for y in range(-100*m, 100*m, m):
        item = cv.find_overlapping(x, y, x, y)
        if len(item) == 1 and item[0] == 5:
            count += 1


print(count)