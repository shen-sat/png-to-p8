def same_color_corner_pixel(pixel, pixel_data, is_origin_pixel=True):
  y = pixel[0]
  x = pixel[1]
  color = pixel[2]

  #does next corner pixel exist?
  try:
    corner_pixel = pixel_data[y + 1][x + 1]
  except KeyError:
    if is_origin_pixel:
      return None
    else:
      return pixel
  
  #is next corner pixel same color?
  if corner_pixel[2] == color:
    return same_color_corner_pixel(corner_pixel, pixel_data, False)
  else:
    if is_origin_pixel:
      return None
    else:
      return pixel

# Tests

import unittest

class SameColorCornerPixel(unittest.TestCase):

  def test_corner_is_present(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']], 1: [0,1,['•••']], 2: [0,2,['•••']] },
      1: { 0: [1,0,['•••']], 1: [1,1,['XXX']], 2: [1,2,['•••']] },
      2: { 0: [2,0,['•••']], 1: [2,1,['•••']], 2: [2,2,['XXX']] }
    }

    origin_pixel = pixel_data[0][0]
    corner_pixel = pixel_data[2][2]

    result = same_color_corner_pixel(origin_pixel, pixel_data)

    self.assertEqual(result, corner_pixel)

  def test_corner_is_NOT_present(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']], 1: [0,1,['•••']], 2: [0,2,['•••']] },
      1: { 0: [1,0,['•••']], 1: [1,1,['•••']], 2: [1,2,['•••']] },
      2: { 0: [2,0,['•••']], 1: [2,1,['•••']], 2: [2,2,['XXX']] }
    }

    origin_pixel = pixel_data[0][0]

    result = same_color_corner_pixel(origin_pixel, pixel_data)

    self.assertEqual(result, None)

  def test_only_one_pixel_present(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']] }
    }

    origin_pixel = pixel_data[0][0]

    result = same_color_corner_pixel(origin_pixel, pixel_data)

    self.assertEqual(result, None)

  def test_gap_is_present(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']], 1: [0,1,['•••']], 2: [0,2,['•••']] },
      1: { 0: [1,0,['•••']],                   2: [1,2,['•••']] },
      2: { 0: [2,0,['•••']], 1: [2,1,['•••']], 2: [2,2,['XXX']] }
    }

    origin_pixel = pixel_data[0][0]
    corner_pixel = pixel_data[2][2]

    result = same_color_corner_pixel(origin_pixel, pixel_data)

    self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()

  

