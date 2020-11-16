from led8x8m import LedMatrix
from led8x8m.grid import GridWalker

ledmx = LedMatrix()

gw = GridWalker(-1, -1)

x, y = gw.get_pos()

ledmx.xy_on(x, y)
