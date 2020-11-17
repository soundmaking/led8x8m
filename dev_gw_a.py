from time import sleep
from led8x8m import LedMatrix
from led8x8m.grid import GridWalker

ledmx = LedMatrix()

gw = GridWalker(7, 0)

while True:
    for _ in range(7):
        gw.move()
        x, y = gw.get_pos()

        ledmx.xy_on(x, y)
        sleep(0.1)
    gw.turn_right()
