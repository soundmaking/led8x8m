# led8x8m/__init__.py
import RPi.GPIO as IO
from time import sleep


class LedMatrix():
    PIN_X = (12, 22, 27, 25, 17, 24, 23, 18)
    PIN_Y = (21, 20, 26, 16, 19, 13, 6, 5)
    matrix_buffer = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1],
    ]

    def __init__(self):
        IO.setwarnings(False)
        IO.setmode(IO.BCM)
        for pin_number in self.PIN_X + self.PIN_Y:
            IO.setup(pin_number, IO.OUT)

    def xy_on(self, x, y):
        """x and y are int 0-7"""
        for index, pin in enumerate(self.PIN_X):
            IO.output(pin, 1 if index == x else 0)

        for index, pin in enumerate(self.PIN_Y):
            IO.output(pin, 0 if index == y else 1)

    def buffer_to_pins(self):
        for y, row in enumerate(self.matrix_buffer):
            for x, val in enumerate(row):
                if val:
                    self.xy_on(x, y)
                # sleep(0.00125)


if __name__ == '__main__':
    ledmx = LedMatrix()
    mode = input("\n/! choose mode, xy or buffer (x or b): ")

    while mode == 'x':
        print('\n/! set x and y ... ')
        x = int(input('x (0-7): '))
        y = int(input('y (0-7): '))
        ledmx.xy_on(x, y)

    while mode == 'b':
        ledmx.buffer_to_pins()


    print('error')
