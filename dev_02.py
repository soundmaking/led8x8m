from time import sleep
from random import randint
from led8x8m import LedMatrix

ledmx = LedMatrix()


def rand_xy():
    x = randint(0, 7)
    y = randint(0, 7)
    return x, y


def rand_list():
    my_list = []
    for _ in range(10):
        x, y = rand_xy()
        my_list.append((x, y))
    return my_list


def rand_in_area(cx, cy, rr):
    my_list = []
    for _ in range(10):
        x = cx + randint(-rr, rr)
        y = cy + randint(-rr, rr)

        my_list.append((x, y))
    return my_list


def fixed_area():
    return [
        (1, 1),
        (0, 0),
        (0, 1),
        (0, 2),
        (1, 0),
        (1, 2),
        (2, 0),
        (2, 1),
        (2, 2),
    ]


while 1:
    cx, cy = 5, 4  # rand_xy()
    this_list = rand_in_area(cx, cy, 1)
    for _ in range(10):
        for x, y in this_list:
            ledmx.xy_on(x, y)
            sleep(0.005)
