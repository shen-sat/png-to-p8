import unittest
from square_getter import SquareGetter

class Handle(unittest.TestCase):

  # ---------------------------------------- When corner does not exist ----------------------------------------
  def test_one_pixel(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']] }
    }

    origin_pixel = pixel_data[0][0]

    output = {}

    result = SquareGetter.handle(origin_pixel, pixel_data)

    self.assertEqual(result, 'call next handler with origin pixel')

  def test_corner_is_NOT_present(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']], 1: [0,1,['XXX']], 2: [0,2,['XXX']] },
      1: { 0: [1,0,['XXX']], 1: [1,1,['•••']], 2: [1,2,['XXX']] },
      2: { 0: [2,0,['XXX']], 1: [2,1,['XXX']], 2: [2,2,['XXX']] }
    }

    origin_pixel = pixel_data[0][0]

    output = {}

    result = SquareGetter.handle(origin_pixel, pixel_data)

    self.assertEqual(result, 'call next handler with origin pixel')

  def test_corner_gap_is_present(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']], 1: [0,1,['XXX']], 2: [0,2,['XXX']] },
      1: { 0: [1,0,['XXX']],                   2: [1,2,['XXX']] },
      2: { 0: [2,0,['XXX']], 1: [2,1,['XXX']], 2: [2,2,['XXX']] }
    }

    origin_pixel = pixel_data[0][0]

    output = {}

    result = SquareGetter.handle(origin_pixel, pixel_data)

    self.assertEqual(result, 'call next handler with origin pixel')

  # ---------------------------------------- When fill does not exist ----------------------------------------

  def test_fill_is_NOT_present(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']], 1: [0,1,['•••']] },
      1: { 0: [1,0,['XXX']], 1: [1,1,['XXX']] },
    }

    origin_pixel = pixel_data[0][0]

    output = {}

    result = SquareGetter.handle(origin_pixel, pixel_data)

    self.assertEqual(result, 'call next handler with origin pixel')

  def test_pixel_data_has_gaps(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']]                   },
      1: { 0: [1,0,['XXX']], 1: [1,1,['XXX']] }
    }

    origin_pixel = pixel_data[0][0]

    output = {}

    result = SquareGetter.handle(origin_pixel, pixel_data)

    self.assertEqual(result, 'call next handler with origin pixel')

  # ---------------------------------------- When square exists ----------------------------------------

  def test_rect_is_present(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']], 1: [0,1,['XXX']] },
      1: { 0: [1,0,['XXX']], 1: [1,1,['XXX']] }
    }

    origin_pixel = pixel_data[0][0]

    output = {}

    result = SquareGetter.handle(origin_pixel, pixel_data)

    self.assertEqual(result, 'add to output hash, call get_first_pixel with amended pixel data')

  def test_rect_is_present_within_other_pixels(self):
    pixel_data = {
      0: { 0: [0,0,['•••']], 1: [0,1,['•••']], 2: [0,2,['•••']], 3: [0,3,['•••']], 4: [0,4,['•••']] },
      1: { 0: [1,0,['•••']], 1: [1,1,['XXX']], 2: [1,2,['XXX']], 3: [1,3,['XXX']], 4: [1,4,['•••']] },
      2: { 0: [2,0,['•••']], 1: [2,1,['XXX']], 2: [2,2,['XXX']], 3: [2,3,['XXX']], 4: [2,4,['•••']] },
      3: { 0: [3,0,['•••']], 1: [3,1,['XXX']], 2: [3,2,['XXX']], 3: [3,3,['XXX']], 4: [3,4,['•••']] },
      4: { 0: [4,0,['•••']], 1: [4,1,['•••']], 2: [4,2,['•••']], 3: [4,3,['•••']], 4: [4,4,['•••']] }
    }

    origin_pixel = pixel_data[1][1]

    output = {}

    result = SquareGetter.handle(origin_pixel, pixel_data)

    self.assertEqual(result, 'add to output hash, call get_first_pixel with amended pixel data')

if __name__ == '__main__':
    unittest.main()

  

