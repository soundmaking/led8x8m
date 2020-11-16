import unittest
from led8x8m.grid import GridWalker


class TestGridWalrker(unittest.TestCase):
    def test_create_at_x_y_pos(self):
        gw = GridWalker(1, 2)
        self.assertEqual(gw.x_pos, 1)
        self.assertEqual(gw.y_pos, 2)

    def test_get_pos(self):
        gw = GridWalker(1, 2)
        x, y = gw.get_pos()
        self.assertEqual(x, 1)
        self.assertEqual(y, 2)


if __name__ == '__main__':
    unittest.main()
