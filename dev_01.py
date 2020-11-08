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
    for _ in range(25):
        x, y = rand_xy()
        my_list.append((x, y))
    return my_list


while 1:
    this_list = rand_list()
    for _ in range(15):
        for x, y in this_list:
            ledmx.xy_on(x, y)
            sleep(0.00125)
