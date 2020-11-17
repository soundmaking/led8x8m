from time import sleep
from led8x8m import LedMatrix
from led8x8m.grid import GridWalker

ledmx = LedMatrix()
gw = GridWalker(7, 0)
size = 1
delta = 1
sleep_time = {
    1: 0.1,
    2: 0.05,
    3: 0.025,
    4: 0.0125,
    5: 0.005,
    6: 0.0025,
    7: 0.00125,
}
while True:
    for _ in range(4):
        for _ in range(size):
            gw.move()
            x, y = gw.get_pos()
            ledmx.xy_on(x, y)
            sleep(sleep_time[size])
        gw.turn_right()
    if size in [0, 7]:
        delta *= -1
    size += delta
