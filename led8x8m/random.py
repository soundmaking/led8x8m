from random import randint


def rand_xy():
    x = randint(0, 7)
    y = randint(0, 7)
    return x, y


def rand_list(size=6):
    my_list = []
    for _ in range(size):
        x, y = rand_xy()
        my_list.append((x, y))
    return my_list


def rand_in_area(cx, cy, rr, size=10):
    my_list = []
    for _ in range(size):
        x = cx + randint(-rr, rr)
        y = cy + randint(-rr, rr)

        my_list.append((x, y))
    return my_list
