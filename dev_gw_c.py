from time import sleep
from led8x8m import LedMatrix
from led8x8m.grid import GridWalker
# from led8x8m.random import rand_xy

ledmx = LedMatrix()
gw = GridWalker(0, 0)


# written as thinking ahead... wrap is not in use here
def wrap(xy):
    def wrap(n):
        if n < 0:
            return 7
        if n > 7:
            return 0
    return wrap(xy[0]), wrap(xy[1])


while True:
    for n in range(7):
        gw.move()
        x, y = gw.get_pos()
        ledmx.xy_on(x, y)
        sleep(0.1)
    gw.turn_left()
