def is_column_same_color(row_i, column_i, min_row_i, pixel_data):
  color = pixel_data[row_i][column_i]

  for current_row_i in range(min_row_i, row_i):
    if pixel_data[current_row_i][column_i] != color:
      return False

  return True

def is_row_same_color(row_i, column_i, min_column_i, pixel_data):
  color = pixel_data[row_i][column_i]

  for current_column_i in range(min_column_i, column_i):
    if pixel_data[row_i][current_column_i] != color:
      return False

  return True


# Tests

import unittest

class CreateRectDataCase(unittest.TestCase):

  def test_column_same_color(self):
    pixel_data = {
      0: { 0: [255, 0, 77] },
      1: { 0: [255, 0, 77] },
      2: { 0: [255, 0, 77] }
    }

    result = is_column_same_color(2,0,0,pixel_data)
    
    self.assertEqual(result, True)

  def test_column_not_same_color(self):
    pixel_data = {
      0: { 0: [333, 3, 33] },
      1: { 0: [255, 0, 77] },
      2: { 0: [255, 0, 77] }
    }

    result = is_column_same_color(2,0,0,pixel_data)
    
    self.assertEqual(result, False)

  def test_column_not_same_color(self):
    pixel_data = {
      0: { 0: [255, 0, 77] },
      1: { 0: [333, 3, 33] },
      2: { 0: [255, 0, 77] }
    }

    result = is_column_same_color(2,0,0,pixel_data)
    
    self.assertEqual(result, False)

  def test_column_not_same_color(self):
    pixel_data = {
      0: { 0: [255, 0, 77] },
      1: { 0: [255, 0, 77] },
      2: { 0: [333, 3, 33] }
    }

    result = is_column_same_color(2,0,0,pixel_data)
    
    self.assertEqual(result, False)

  def test_row_is_same_color(self):
    pixel_data = {
      0: { 0: [255, 0, 77], 1: [255, 0, 77], 2: [255, 0, 77] }
    }

    result = is_row_same_color(0,2,0,pixel_data)
    
    self.assertEqual(result, True)

  def test_row_is_not_same_color(self):
    pixel_data = {
      0: { 0: [333, 3, 33], 1: [255, 0, 77], 2: [255, 0, 77] }
    }

    result = is_row_same_color(0,2,0,pixel_data)
    
    self.assertEqual(result, False)

  def test_row_is_not_same_color(self):
    pixel_data = {
      0: { 0: [255, 0, 77], 1: [333, 3, 33], 2: [255, 0, 77] }
    }

    result = is_row_same_color(0,2,0,pixel_data)
    
    self.assertEqual(result, False)

  def test_row_is_not_same_color(self):
    pixel_data = {
      0: { 0: [255, 0, 77], 1: [255, 0, 77], 2: [333, 3, 33] }
    }

    result = is_row_same_color(0,2,0,pixel_data)
    
    self.assertEqual(result, False)

if __name__ == '__main__':
    unittest.main()

  

