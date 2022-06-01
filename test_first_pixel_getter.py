import unittest
from first_pixel_getter import EmptyPixelDataException
from first_pixel_getter import FirstPixelGetter


class Handle(unittest.TestCase):

  def test_empty(self):
    pixel_data = {
      0: {},
      1: {}
    }

    self.assertRaises(EmptyPixelDataException, FirstPixelGetter.handle, pixel_data)

  def test_one_pixel_in_first_row(self):
    pixel_data = {
      0: { 0: 'first pixel' },
      1: {},
      2: {}
    }

    result = FirstPixelGetter.handle(pixel_data)
    self.assertEqual(result, [0,0])

  def test_one_pixel_NOT_in_first_row(self):
    pixel_data = {
      0: {},
      1: { 127: 'first pixel' },
      2: {}
    }

    result = FirstPixelGetter.handle(pixel_data)
    self.assertEqual(result, [1,127])

  def test_two_pixels_in_a_row(self):
    pixel_data = {
      0: {},
      1: {},
      2: { 50: 'first pixel', 100: 'another pixel' }
    }

    result = FirstPixelGetter.handle(pixel_data)
    self.assertEqual(result, [2,50])

  def test_pixels_in_more_than_one_row(self):
    pixel_data = {
      0: { 2: 'first pixel', 3: 'another pixel' },
      1: {},
      2: { 50: 'yet another pixel', 100: 'final pixel' }
    }

    result = FirstPixelGetter.handle(pixel_data)
    self.assertEqual(result, [0,2])

if __name__ == '__main__':
    unittest.main()

  

