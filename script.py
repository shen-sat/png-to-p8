import cv2 as cv

def create_pixel_data(image):
  result = {}
  for y_index, row in enumerate(image):
    y = y_index
    for x_index, column in enumerate(row):
      x = x_index
      if x in result:
        result[x][y] = [column[2],column[1],column[0]]
      else:
        result[x] = {}
        result[x][y] = [column[2],column[1],column[0]]

  return result

# Tests

import unittest

class PngToP8TestCase(unittest.TestCase):

  def test_create_pixel_data(self):  
    
    image = cv.imread('2x2-red-blue-green-yellow.png')
    result = create_pixel_data(image)
    expected_result = {
      0: { 0: [255, 0, 77], 1: [0, 228, 54] },
      1: { 0: [41, 173, 255], 1: [255, 236, 39] }
    }
    self.assertEqual(result, expected_result)

