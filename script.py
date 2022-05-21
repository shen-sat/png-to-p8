import cv2 as cv

def create_pixel_data(image):
  pixel_data = {}
  for row_index, row in enumerate(image):
    for cell_index, cell in enumerate(row):
      if cell_index in pixel_data:
        pixel_data[cell_index][row_index] = [cell[2],cell[1],cell[0]]
      else:
        pixel_data[cell_index] = {}
        pixel_data[cell_index][row_index] = [cell[2],cell[1],cell[0]]

  return pixel_data

# Tests

import unittest

class CreatePixelDataCase(unittest.TestCase):

  def test_2x2_red_blue_green_yellow(self):
    
    image = cv.imread('2x2-red-blue-green-yellow.png')
    result = create_pixel_data(image)
    expected_result = {
      0: { 0: [255, 0, 77], 1: [0, 228, 54] },
      1: { 0: [41, 173, 255], 1: [255, 236, 39] }
    }
    self.assertEqual(result, expected_result)

  def test_1x1_red(self):
    
    image = cv.imread('1x1-red.png')
    result = create_pixel_data(image)
    expected_result = {
      0: { 0: [255, 0, 77]}
    }
    self.assertEqual(result, expected_result)

