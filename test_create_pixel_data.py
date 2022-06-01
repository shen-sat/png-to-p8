import unittest
from create_pixel_data import CreatePixelData

class CreatePixelDataCase(unittest.TestCase):

  def test_1x1_red(self):
    result = CreatePixelData.create_pixel_data('1x1-red.png')

    expected_result = {
      0: { 0:[255,0,77] }
    }
    self.assertEqual(result, expected_result)

  def test_2x2_red(self):
    result = CreatePixelData.create_pixel_data('2x2-red.png')
    
    expected_result = {
      0: { 0: [255,0,77], 1: [255,0,77] },
      1: { 0: [255,0,77], 1: [255,0,77] }
    }
    self.assertEqual(result, expected_result)

  def test_2x2_red_red_blue_blue(self):
    result = CreatePixelData.create_pixel_data('2x2-red-red-blue-blue.png')
    
    expected_result = {
      0: { 0: [255,0,77],   1: [255,0,77] },
      1: { 0: [41,173,255], 1: [41,173,255] }
    }
    self.assertEqual(result, expected_result)

  def test_2x2_red_blue_red_blue(self):
    result = CreatePixelData.create_pixel_data('2x2-red-blue-red-blue.png')
    
    expected_result = {
      0: { 0: [255,0,77], 1: [41,173,255] },
      1: { 0: [255,0,77], 1: [41,173,255] }
    }
    self.assertEqual(result, expected_result)

  def test_2x2_red_blue_green_yellow(self):
    result = CreatePixelData.create_pixel_data('2x2-red-blue-green-yellow.png')
    
    expected_result = {
      0: { 0: [255,0,77], 1: [41,173,255] },
      1: { 0: [0,228,54], 1: [255,236,39] }
    }
    self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

  

