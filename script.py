import cv2 as cv

def create_pixel_data(image):
  pixel_data = {}
  for y, row in enumerate(image):
    for x, column in enumerate(row):
      if y in pixel_data:
        pixel_data[y][x] = [column[2],column[1],column[0]]
      else:
        pixel_data[y] = {}
        pixel_data[y][x] = [column[2],column[1],column[0]]

  return pixel_data

# Tests

import unittest

class CreatePixelDataCase(unittest.TestCase):

  def test_1x1_red(self):
    
    image = cv.imread('1x1-red.png')
    result = create_pixel_data(image)
    expected_result = {
      0: { 0:[255,0,77] }
    }
    self.assertEqual(result, expected_result)

  def test_2x2_red(self):
    
    image = cv.imread('2x2-red.png')
    result = create_pixel_data(image)
    expected_result = {
      0: { 0: [255,0,77], 1: [255,0,77] },
      1: { 0: [255,0,77], 1: [255,0,77] }
    }
    self.assertEqual(result, expected_result)

  def test_2x2_red_red_blue_blue(self):
    
    image = cv.imread('2x2-red-red-blue-blue.png')
    result = create_pixel_data(image)
    expected_result = {
      0: { 0: [255,0,77],   1: [255,0,77] },
      1: { 0: [41,173,255], 1: [41,173,255] }
    }
    self.assertEqual(result, expected_result)

  def test_2x2_red_blue_red_blue(self):
    
    image = cv.imread('2x2-red-blue-red-blue.png')
    result = create_pixel_data(image)
    expected_result = {
      0: { 0: [255,0,77], 1: [41,173,255] },
      1: { 0: [255,0,77], 1: [41,173,255] }
    }
    self.assertEqual(result, expected_result)

  def test_2x2_red_blue_green_yellow(self):
    
    image = cv.imread('2x2-red-blue-green-yellow.png')
    result = create_pixel_data(image)
    expected_result = {
      0: { 0: [255,0,77], 1: [41,173,255] },
      1: { 0: [0,228,54], 1: [255,236,39] }
    }
    self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

  

