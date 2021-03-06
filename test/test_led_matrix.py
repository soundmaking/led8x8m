import unittest
from led8x8m import LedMatrix


class TestLedMatrix(unittest.TestCase):
    def test_pin_numbers(self):
        self.assertEqual(len(LedMatrix.PIN_X), 8)
        self.assertEqual(len(LedMatrix.PIN_Y), 8)
        set_x = set(LedMatrix.PIN_X)
        set_y = set(LedMatrix.PIN_Y)
        self.assertEqual(len(set_x), 8)
        self.assertEqual(len(set_y), 8)
        self.assertTrue(set_x.isdisjoint(set_y))

    def test_matrix_buffer(self):
        self.assertIsInstance(LedMatrix.matrix_buffer, list)
        self.assertEqual(len(LedMatrix.matrix_buffer), 8)
        for n in range(8):
            self.assertIsInstance(LedMatrix.matrix_buffer[n], list)
            self.assertEqual(len(LedMatrix.matrix_buffer[n]), 8)
