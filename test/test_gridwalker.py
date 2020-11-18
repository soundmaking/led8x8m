import unittest
from led8x8m.grid import GridWalker, Direction


class TestGridWalker(unittest.TestCase):
    def test_create_at_x_y_pos(self):
        gw = GridWalker(1, 2)
        self.assertEqual(gw.x_pos, 1)
        self.assertEqual(gw.y_pos, 2)

    def test_get_pos(self):
        gw = GridWalker(1, 2)
        x, y = gw.get_pos()
        self.assertEqual(x, 1)
        self.assertEqual(y, 2)

    def test_move(self):
        gw = GridWalker(1, 2)
        self.assertEqual(gw.direction, Direction.S)
        gw.move(1)
        x, y = gw.get_pos()
        self.assertEqual(x, 1)
        self.assertEqual(y, 3)

    def test_direction_init(self):
        gw = GridWalker(1, 2)
        self.assertEqual(gw.direction, Direction.S)

    def test_direction_turn_right(self):
        gw = GridWalker(1, 2)
        self.assertEqual(gw.direction, Direction.S)
        gw.turn_right()
        self.assertEqual(gw.direction, Direction.W)
        gw.turn_right()
        self.assertEqual(gw.direction, Direction.N)
        gw.turn_right()
        self.assertEqual(gw.direction, Direction.E)
        gw.turn_right()
        self.assertEqual(gw.direction, Direction.S)

    def test_direction_turn_left(self):
        gw = GridWalker(1, 2)
        self.assertEqual(gw.direction, Direction.S)
        gw.turn_left()
        self.assertEqual(gw.direction, Direction.E)
        gw.turn_left()
        self.assertEqual(gw.direction, Direction.N)
        gw.turn_left()
        self.assertEqual(gw.direction, Direction.W)
        gw.turn_left()
        self.assertEqual(gw.direction, Direction.S)


class TestDirection(unittest.TestCase):
    def test_direction(self):
        self.assertEqual(Direction.N, (0, -1))
        self.assertEqual(Direction.S, (0, 1))
        self.assertEqual(Direction.W, (-1, 0))
        self.assertEqual(Direction.E, (1, 0))


if __name__ == '__main__':
    unittest.main()
