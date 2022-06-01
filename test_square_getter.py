import unittest
from square_getter import SquareGetter

class Handle(unittest.TestCase):

# ---------------------------------------- When square does not exist ----------------------------------------

  def test_one_pixel(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']] }
    }

    origin_pixel = pixel_data[0][0]

    result = SquareGetter.handle(origin_pixel, pixel_data)

    self.assertEqual(result, 'call next handler with origin pixel and pixel data')

  def test_square_is_not_present_FILL_CENTER(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']], 1: [0,1,['XXX']], 2: [0,2,['XXX']] },
      1: { 0: [1,0,['XXX']], 1: [1,1,['•••']], 2: [1,2,['XXX']] },
      2: { 0: [2,0,['XXX']], 1: [2,1,['XXX']], 2: [2,2,['XXX']] }
    }

    origin_pixel = pixel_data[0][0]

    result = SquareGetter.handle(origin_pixel, pixel_data)

    self.assertEqual(result, 'call next handler with origin pixel and pixel data')

  def test_square_is_not_present_GAP_CENTER(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']], 1: [0,1,['XXX']], 2: [0,2,['XXX']] },
      1: { 0: [1,0,['XXX']],                   2: [1,2,['XXX']] },
      2: { 0: [2,0,['XXX']], 1: [2,1,['XXX']], 2: [2,2,['XXX']] }
    }

    origin_pixel = pixel_data[0][0]

    result = SquareGetter.handle(origin_pixel, pixel_data)

    self.assertEqual(result, 'call next handler with origin pixel and pixel data')

  def test_square_is_not_present_FILL_CORNER(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']], 1: [0,1,['•••']] },
      1: { 0: [1,0,['XXX']], 1: [1,1,['XXX']] },
    }

    origin_pixel = pixel_data[0][0]

    result = SquareGetter.handle(origin_pixel, pixel_data)

    self.assertEqual(result, 'call next handler with origin pixel and pixel data')

  def test_square_is_not_present_GAP_CORNER(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']],  1: [0,1,['XXX']] },
      1: { 0: [1,0,['XXX']]                  }
    }

    origin_pixel = pixel_data[0][0]

    result = SquareGetter.handle(origin_pixel, pixel_data)

    self.assertEqual(result, 'call next handler with origin pixel and pixel data')


  def test_vertical_and_horizontal_lines_and_pixels_only(self):
    pixel_data = {
      1: { 21: [1,21,['$$$']], 22: [1,22,['+++']], 23: [1,23,['@@@']] },
      2: { 21: [2,21,['XXX']], 22: [2,22,['!!!']], 23: [2,23,['&&&']] },
      3: { 21: [3,21,['XXX']], 22: [3,22,['•••']], 23: [3,23,['•••']] }
    }

    origin_pixel = pixel_data[1][21]

    result = SquareGetter.handle(origin_pixel, pixel_data)

    self.assertEqual(result, 'call next handler with origin pixel and pixel data')

  # ---------------------------------------- When square exists ----------------------------------------

  def test_square_is_present(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']], 1: [0,1,['XXX']] },
      1: { 0: [1,0,['XXX']], 1: [1,1,['XXX']] }
    }

    origin_pixel = pixel_data[0][0]

    result = SquareGetter.handle(origin_pixel, pixel_data)

    self.assertEqual(result, 'call pixel chomper with start and end pixels')

  def test_square_is_present_within_other_pixels(self):
    pixel_data = {
      0: { 0: [0,0,['•••']], 1: [0,1,['•••']], 2: [0,2,['•••']], 3: [0,3,['•••']], 4: [0,4,['•••']] },
      1: { 0: [1,0,['•••']], 1: [1,1,['XXX']], 2: [1,2,['XXX']], 3: [1,3,['XXX']], 4: [1,4,['•••']] },
      2: { 0: [2,0,['•••']], 1: [2,1,['XXX']], 2: [2,2,['XXX']], 3: [2,3,['XXX']], 4: [2,4,['•••']] },
      3: { 0: [3,0,['•••']], 1: [3,1,['XXX']], 2: [3,2,['XXX']], 3: [3,3,['XXX']], 4: [3,4,['•••']] },
      4: { 0: [4,0,['•••']], 1: [4,1,['•••']], 2: [4,2,['•••']], 3: [4,3,['•••']], 4: [4,4,['•••']] }
    }

    origin_pixel = pixel_data[1][1]

    result = SquareGetter.handle(origin_pixel, pixel_data)

    self.assertEqual(result, 'call pixel chomper with start and end pixels')

if __name__ == '__main__':
    unittest.main()

  

