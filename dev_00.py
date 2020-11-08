import RPi.GPIO as IO

PIN_X = (12, 22, 27, 25, 17, 24, 23, 18)
PIN_Y = (21, 20, 26, 16, 19, 13, 6, 5)

IO.setwarnings(False)
IO.setmode(IO.BCM)

for pin_number in PIN_X + PIN_Y:
    IO.setup(pin_number, IO.OUT)

print('input x and y coordinate to choose an LED in the 8x8 matrix')

while 1:
    print('\n/! set x and y ... ')

    x = int(input('x (0-7): '))
    y = int(input('y (0-7): '))

    for index, pin in enumerate(PIN_X):
        IO.output(pin, 1 if index == x else 0)

    for index, pin in enumerate(PIN_Y):
        IO.output(pin, 0 if index == y else 1)
