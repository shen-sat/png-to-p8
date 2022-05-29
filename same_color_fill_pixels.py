class PixelNotFound(Exception):
  pass

class OriginSameRowAsCorner(Exception):
  pass

class OriginSameColumnAsCorner(Exception):
  pass

def is_rect(origin_pixel, corner_pixel, pixel_data):
  if origin_pixel[0] == corner_pixel[0]:
    raise OriginSameRowAsCorner(f'origin: {origin_pixel}, corner: {corner_pixel}')
  elif origin_pixel[1] == corner_pixel[1]:
    raise OriginSameColumnAsCorner(f'origin: {origin_pixel}, corner: {corner_pixel}')

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
        raise PixelNotFound(f'y:{y}, x:{x}')

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

  def test_rect_is_present(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']], 1: [0,1,['XXX']] },
      1: { 0: [1,0,['XXX']], 1: [1,1,['XXX']] }
    }

    origin_pixel = pixel_data[0][0]
    corner_pixel = pixel_data[1][1]

    result = is_rect(origin_pixel, corner_pixel, pixel_data)

    self.assertEqual(result, True)

  def test_rect_is_NOT_present(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']], 1: [0,1,['•••']] },
      1: { 0: [1,0,['•••']], 1: [1,1,['XXX']] },
    }

    origin_pixel = pixel_data[0][0]
    corner_pixel = pixel_data[1][1]

    result = is_rect(origin_pixel, corner_pixel, pixel_data)

    self.assertEqual(result, False)

  def test_rect_is_present_within_other_pixels(self):
    pixel_data = {
      0: { 0: [0,0,['•••']], 1: [0,1,['•••']], 2: [0,2,['•••']], 3: [0,3,['•••']], 4: [0,4,['•••']] },
      1: { 0: [1,0,['•••']], 1: [1,1,['XXX']], 2: [1,2,['XXX']], 3: [1,3,['XXX']], 4: [1,4,['•••']] },
      2: { 0: [2,0,['•••']], 1: [2,1,['XXX']], 2: [2,2,['XXX']], 3: [2,3,['XXX']], 4: [2,4,['•••']] },
      3: { 0: [3,0,['•••']], 1: [3,1,['XXX']], 2: [3,2,['XXX']], 3: [3,3,['XXX']], 4: [3,4,['•••']] },
      4: { 0: [4,0,['•••']], 1: [4,1,['•••']], 2: [4,2,['•••']], 3: [4,3,['•••']], 4: [4,4,['•••']] }
    }

    origin_pixel = pixel_data[1][1]
    corner_pixel = pixel_data[3][3]

    result = is_rect(origin_pixel, corner_pixel, pixel_data)

    self.assertEqual(result, True)

  def test_pixel_data_has_gaps(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']]                   },
      1: { 0: [1,0,['XXX']], 1: [1,1,['XXX']] }
    }

    origin_pixel = pixel_data[0][0]
    corner_pixel = pixel_data[1][1]

    with self.assertRaises(PixelNotFound) as context:
      is_rect(origin_pixel, corner_pixel, pixel_data)

    self.assertTrue('y:0, x:1' in str(context.exception))

  def test_origin_same_row_as_corner(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']], 1: [0,1,['XXX']] }
    }

    origin_pixel = pixel_data[0][0]
    corner_pixel = pixel_data[0][1]

    with self.assertRaises(OriginSameRowAsCorner) as context:
      is_rect(origin_pixel, corner_pixel, pixel_data)

    self.assertTrue("origin: [0, 0, ['XXX']], corner: [0, 1, ['XXX']]" in str(context.exception))

  def test_origin_same_column_as_corner(self):
    pixel_data = {
      0: { 0: [0,0,['XXX']] },
      1: { 0: [1,0,['XXX']] },
    }

    origin_pixel = pixel_data[0][0]
    corner_pixel = pixel_data[1][0]

    with self.assertRaises(OriginSameColumnAsCorner) as context:
      is_rect(origin_pixel, corner_pixel, pixel_data)

    self.assertTrue("origin: [0, 0, ['XXX']], corner: [1, 0, ['XXX']]" in str(context.exception))

if __name__ == '__main__':
    unittest.main()

  

