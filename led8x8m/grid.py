

class GridWalker(object):
    def __init__(self, start_x, start_y):
        self.x_pos = start_x
        self.y_pos = start_y
        self.direction = Direction.S

    def get_pos(self):
        return self.x_pos, self.y_pos

    def move(self, step_size=1):
        d_x, d_y = self.direction
        self.x_pos += d_x
        self.y_pos += d_y

    def turn_right(self):
        options = {
            Direction.S: Direction.W,
            Direction.W: Direction.N,
            Direction.N: Direction.E,
            Direction.E: Direction.S,
        }
        self.direction = options[self.direction]


class Direction(object):
    N = (0, -1)
    S = (0, 1)
    W = (-1, 0)
    E = (1, 0)
