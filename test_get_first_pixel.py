import unittest
from get_first_pixel import GetFirstPixel

class Handle(unittest.TestCase):

  def test_empty_pixel_data(self):
    pixel_data = {
      0: {},
      1: {}
    }
    output = {}

    result = GetFirstPixel.handle(pixel_data, output)
    self.assertEqual(result, 'all pixel data processed')

  def test_pixel_data_with_one_pixel_in_first_row(self):
    pixel_data = {
      0: { 0: 'first pixel' },
      1: {},
      2: {}
    }
    output = {}

    result = GetFirstPixel.handle(pixel_data, output)
    self.assertEqual(result, 'first pixel')

  def test_pixel_data_with_one_pixel_NOT_in_first_row(self):
    pixel_data = {
      0: {},
      1: { 127: 'first pixel' },
      2: {}
    }
    output = {}

    result = GetFirstPixel.handle(pixel_data, output)
    self.assertEqual(result, 'first pixel')

  def test_pixel_data_with_two_pixels_in_a_row(self):
    pixel_data = {
      0: {},
      1: {},
      2: { 50: 'first pixel', 100: 'another pixel' }
    }
    output = {}

    result = GetFirstPixel.handle(pixel_data, output)
    self.assertEqual(result, 'first pixel')

  def test_pixel_data_with_pixels_in_more_than_one_row(self):
    pixel_data = {
      0: { 2: 'first pixel', 3: 'another pixel' },
      1: {},
      2: { 50: 'yet another pixel', 100: 'final pixel' }
    }
    output = {}

    result = GetFirstPixel.handle(pixel_data, output)
    self.assertEqual(result, 'first pixel')

if __name__ == '__main__':
    unittest.main()

  

