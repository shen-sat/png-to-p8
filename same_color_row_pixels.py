def same_color_row_pixels(origin_pixel, corner_pixel, pixel_data):
  min_x = origin_pixel[1]
  max_x = corner_pixel[1]
  y = corner_pixel[0]
  color = corner_pixel[2]

  
  pixels = []

  for x in range(min_x, max_x):
    try:
      next_pixel = pixel_data[y][x]
    except KeyError:
      return None

    if pixel_data[y][x][2] == color:
      pixels += [ next_pixel ] 
    else:
      return None

  return pixels



# Tests

import unittest

class SameColorRowPixels(unittest.TestCase):

  def test_row_is_same_color(self):
    pixel_data = {
      0: { 0: [0,0,[255,0,77]], 1: [0,1,[255,0,77]] },
      1: { 0: [1,0,[255,0,77]], 1: [1,1,[255,0,77]] }
    }

    origin_pixel = pixel_data[0][0]
    corner_pixel = pixel_data[1][1]
    expected_result = [ [1,0,[255,0,77]] ]


    result = same_color_row_pixels(origin_pixel, corner_pixel, pixel_data)

    self.assertEqual(result, expected_result)

  def test_row_is_NOT_same_color(self):
    pixel_data = {
      0: { 0: [0,0,[255,0,77]], 1: [0,1,[255,0,77]] },
      1: { 0: [1,0,[333,3,33]], 1: [1,1,[255,0,77]] }
    }

    origin_pixel = pixel_data[0][0]
    corner_pixel = pixel_data[1][1]


    result = same_color_row_pixels(origin_pixel, corner_pixel, pixel_data)

    self.assertEqual(result, None)

  def test_row_has_gaps(self):
    pixel_data = {
      0: { 0: [0,0,[255,0,77]], 1: [0,1,[255,0,77]] },
      1: {                      1: [1,1,[255,0,77]] }
    }

    origin_pixel = pixel_data[0][0]
    corner_pixel = pixel_data[1][1]


    result = same_color_row_pixels(origin_pixel, corner_pixel, pixel_data)

    self.assertEqual(result, None)

  def test_large_square_row_same_color(self):
    pixel_data = {
      0: { 0: [0,0,[255,0,77]], 1: [0,1,[255,0,77]], 2: [0,2,[255,0,77]] },
      1: { 0: [1,0,[255,0,77]], 1: [1,1,[255,0,77]], 2: [1,2,[255,0,77]] },
      2: { 0: [2,0,[255,0,77]], 1: [2,1,[255,0,77]], 2: [2,2,[255,0,77]] }
    }

    origin_pixel = pixel_data[0][0]
    corner_pixel = pixel_data[2][2]
    expected_result = [
      [2,0,[255,0,77]], [2,1,[255,0,77]]
    ]


    result = same_color_row_pixels(origin_pixel, corner_pixel, pixel_data)

    self.assertEqual(result, expected_result)