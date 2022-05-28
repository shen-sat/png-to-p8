def same_color_fill_pixels(origin_pixel, corner_pixel, pixel_data):
  min_y = origin_pixel[0]
  min_x = origin_pixel[1]
  color = origin_pixel[2]

  max_y = corner_pixel[0]
  max_x = corner_pixel[1]

  pixels = []

  for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
      print(f'for {y} and {x} trying to get pixel...')
      try:
        pixel = pixel_data[y][x]
      except KeyError:
        print('pixel does not exist')
        return None    

      if pixel == origin_pixel:
        print('pixel is origin')
        continue
      elif pixel == corner_pixel:
        print('pixel is corner')
        return pixels
      else:
        print('adding pixel to pixels')
        if pixel[2] == color:
          pixels += [ pixel ]
        else:
          print('pixel is not required color')
          return pixels

# Tests

import unittest

class SameColorFillPixels(unittest.TestCase):

  def test_corner_is_present(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']], 1: [0,1,['XXX']] },
      1: { 0: [1,0,['XXX']], 1: [1,1,['XXX']] }
    }

    origin_pixel = pixel_data[0][0]
    corner_pixel = pixel_data[1][1]
    expected_result = [
      [0,1,['XXX']],
      [1,0,['XXX']] 
    ]

    result = same_color_fill_pixels(origin_pixel, corner_pixel, pixel_data)

    self.assertEqual(result, expected_result)

  # def test_corner_is_NOT_present(self):
  #   pixel_data = {
  #     0: { 0: [0,0,['XXX']], 1: [0,1,['•••']], 2: [0,2,['•••']] },
  #     1: { 0: [1,0,['•••']], 1: [1,1,['•••']], 2: [1,2,['•••']] },
  #     2: { 0: [2,0,['•••']], 1: [2,1,['•••']], 2: [2,2,['XXX']] }
  #   }

  #   origin_pixel = pixel_data[0][0]

  #   result = same_color_fill_pixels(origin_pixel, pixel_data)

  #   self.assertEqual(result, None)

  # def test_only_one_pixel_present(self):
  #   pixel_data = {
  #     0: { 0: [0,0,['XXX']] }
  #   }

  #   origin_pixel = pixel_data[0][0]

  #   result = same_color_fill_pixels(origin_pixel, pixel_data)

  #   self.assertEqual(result, None)

  # def test_gap_is_present(self):
  #   pixel_data = {
  #     0: { 0: [0,0,['XXX']], 1: [0,1,['•••']], 2: [0,2,['•••']] },
  #     1: { 0: [1,0,['•••']],                   2: [1,2,['•••']] },
  #     2: { 0: [2,0,['•••']], 1: [2,1,['•••']], 2: [2,2,['XXX']] }
  #   }

  #   origin_pixel = pixel_data[0][0]
  #   corner_pixel = pixel_data[2][2]

  #   result = same_color_fill_pixels(origin_pixel, pixel_data)

  #   self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()

  

