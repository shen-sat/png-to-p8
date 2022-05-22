import cv2 as cv

def is_column_same_color(row, column, min_row, pixel_data):
  color = pixel_data[row][column]

  for current_row in range(min_row,(row + 1)):
    if pixel_data[current_row][column] != color:
      return False

  return True


# Tests

import unittest

class CreateRectDataCase(unittest.TestCase):

  def test_is_column_same_color(self):
    pixel_data = {
      0: { 0: [255, 0, 77], 1: [255, 0, 77] },
      1: { 0: [255, 0, 77], 1: [255, 0, 77] },
      2: { 0: [255, 0, 77], 1: [255, 0, 77] }
    }

    result = is_column_same_color(2,1,0,pixel_data)
    
    self.assertEqual(result, True)

if __name__ == '__main__':
    unittest.main()

  

