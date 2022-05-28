class PixelNotFound(Exception):
    pass



def is_rect(origin_pixel, corner_pixel, pixel_data):
  min_y = origin_pixel[0]
  min_x = origin_pixel[1]
  color = origin_pixel[2]

  max_y = corner_pixel[0]
  max_x = corner_pixel[1]

  for y in range(min_y, max_y + 1):
    for x in range(min_x, max_x + 1):
      try:
        print(f'checking pixel at y:{y}, x:{x}...')
        pixel = pixel_data[y][x]
      except KeyError:
        raise PixelNotFound(f'y:{y} and x:{x}')

      if pixel == origin_pixel:
        print('pixel is origin')
        continue
      elif pixel == corner_pixel:
        print('pixel is corner, so we have finished!')
        return True
      else:
        if pixel[2] != color:
          print(f'pixel:{pixel} is not same color as origin_pixel:{origin_pixel}')
          return False

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

    result = is_rect(origin_pixel, corner_pixel, pixel_data)

    self.assertEqual(result, True)

  # def test_corner_is_NOT_present(self):
  #   pixel_data = {
  #     0: { 0: [0,0,['XXX']], 1: [0,1,['•••']], 2: [0,2,['•••']] },
  #     1: { 0: [1,0,['•••']], 1: [1,1,['•••']], 2: [1,2,['•••']] },
  #     2: { 0: [2,0,['•••']], 1: [2,1,['•••']], 2: [2,2,['XXX']] }
  #   }

  #   origin_pixel = pixel_data[0][0]

  #   result = is_rect(origin_pixel, pixel_data)

  #   self.assertEqual(result, None)

  # def test_only_one_pixel_present(self):
  #   pixel_data = {
  #     0: { 0: [0,0,['XXX']] }
  #   }

  #   origin_pixel = pixel_data[0][0]

  #   result = is_rect(origin_pixel, pixel_data)

  #   self.assertEqual(result, None)

  # def test_gap_is_present(self):
  #   pixel_data = {
  #     0: { 0: [0,0,['XXX']], 1: [0,1,['•••']], 2: [0,2,['•••']] },
  #     1: { 0: [1,0,['•••']],                   2: [1,2,['•••']] },
  #     2: { 0: [2,0,['•••']], 1: [2,1,['•••']], 2: [2,2,['XXX']] }
  #   }

  #   origin_pixel = pixel_data[0][0]
  #   corner_pixel = pixel_data[2][2]

  #   result = is_rect(origin_pixel, pixel_data)

  #   self.assertEqual(result, None)

if __name__ == '__main__':
    unittest.main()

  

