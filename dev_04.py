from time import sleep
from random import randint
from led8x8m import LedMatrix
from led8x8m.random import rand_in_area, rand_xy

ledmx = LedMatrix()

counter = 0
while 1:
    counter = counter + 1 if counter < 6 else 1
    if counter == 1:
        cx, cy = rand_xy()
    this_list = rand_in_area(
        cx,
        cy,
        randint(1, 3),
        randint(6, 13),
    )
    for _ in range(10):
        for x, y in this_list:
            ledmx.xy_on(x, y)
            sleep(0.002)
