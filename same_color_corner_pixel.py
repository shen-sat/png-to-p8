# def same_color_column(row_i, column_i, min_row_i, pixel_data):
#   color = pixel_data[row_i][column_i]
#   column = []

#   for current_row_i in range(min_row_i, row_i):
#     if pixel_data[current_row_i][column_i] == color:
#       column + [ pixel_data[current_row_i][column_i] ]
#     else:
      

#   return True



def same_color_corner_pixel(pixel, pixel_data):
  y = pixel[0]
  x = pixel[1]
  color = pixel[2]

  try:
      corner_pixel = pixel_data[y + 1][x + 1]
  except KeyError:
      return None
  
  if corner_pixel[2] == color:
    return corner_pixel
  else:
    return None

# Tests

import unittest

class SameColorCornerPixel(unittest.TestCase):

  def test_corner_is_same_color(self):
    pixel_data = {
      0: { 0: [0,0,[255,0,77]], 1: [0,1,[255,0,77]] },
      1: { 0: [1,0,[255,0,77]], 1: [1,1,[255,0,77]] }
    }

    origin_pixel = pixel_data[0][0]
    corner_pixel = pixel_data[1][1]

    result = same_color_corner_pixel(origin_pixel, pixel_data)

    self.assertEqual(result, corner_pixel)

  def test_corner_is_NOT_same_color(self):
    pixel_data = {
      0: { 0: [0,0,[255,0,77]], 1: [0,1,[255,0,77]] },
      1: { 0: [1,0,[255,0,77]], 1: [1,1,[333,3,33]] }
    }

    origin_pixel = pixel_data[0][0]

    result = same_color_corner_pixel(origin_pixel, pixel_data)

    self.assertEqual(result, None)

  def test_corner_is_out_of_bounds(self):
    pixel_data = {
      0: { 0: [0,0,[255,0,77]], 1: [0,1,[255,0,77]] },
      1: { 0: [1,0,[255,0,77]], 1: [1,1,[255,0,77]] }
    }

    origin_pixel = pixel_data[1][1]

    result = same_color_corner_pixel(origin_pixel, pixel_data)

    self.assertEqual(result, None)


  # def test_column_same_color(self):
  #   pixel_data = {
  #     0: { 0: [255, 0, 77] },
  #     1: { 0: [255, 0, 77] },
  #     2: { 0: [255, 0, 77] }
  #   }

  #   result = same_color_column(2,0,0,pixel_data)
    
  #   self.assertEqual(result, True)

  # def test_column_not_same_color(self):
  #   pixel_data = {
  #     0: { 0: [333, 3, 33] },
  #     1: { 0: [255, 0, 77] },
  #     2: { 0: [255, 0, 77] }
  #   }

  #   result = same_color_column(2,0,0,pixel_data)
    
  #   self.assertEqual(result, False)

  # def test_column_not_same_color1(self):
  #   pixel_data = {
  #     0: { 0: [255, 0, 77] },
  #     1: { 0: [333, 3, 33] },
  #     2: { 0: [255, 0, 77] }
  #   }

  #   result = same_color_column(2,0,0,pixel_data)
    
  #   self.assertEqual(result, False)

  # def test_column_not_same_color2(self):
  #   pixel_data = {
  #     0: { 0: [255, 0, 77] },
  #     1: { 0: [255, 0, 77] },
  #     2: { 0: [333, 3, 33] }
  #   }

  #   result = same_color_column(2,0,0,pixel_data)
    
  #   self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()

  

