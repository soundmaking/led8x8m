

class GridWalker(object):
    def __init__(self, start_x, start_y):
        self.x_pos = start_x
        self.y_pos = start_y

    def get_pos(self):
        return self.x_pos, self.y_pos
