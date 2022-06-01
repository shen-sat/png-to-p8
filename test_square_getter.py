import unittest
from square_getter import SquareGetter

class Handle(unittest.TestCase):

# ---------------------------------------- When square does not exist ----------------------------------------

  def test_one_pixel(self):
    pixel_data = {
      0: { 0: ['XXX'] }
    }

    origin = [0,0]

    result = SquareGetter.handle(origin, pixel_data)

    self.assertEqual(result, 'call next handler with origin pixel and pixel data')

  def test_center_different(self):
    pixel_data = {
      0: { 0: ['XXX'], 1: ['XXX'], 2: ['XXX'] },
      1: { 0: ['XXX'], 1: ['•••'], 2: ['XXX'] },
      2: { 0: ['XXX'], 1: ['XXX'], 2: ['XXX'] }
    }

    origin = [0,0] 

    result = SquareGetter.handle(origin, pixel_data)

    self.assertEqual(result, 'call next handler with origin pixel and pixel data')

  def test_gap_center(self):
    pixel_data = {
      0: { 0: ['XXX'], 1: ['XXX'], 2: ['XXX'] },
      1: { 0: ['XXX'],             2: ['XXX'] },
      2: { 0: ['XXX'], 1: ['XXX'], 2: ['XXX'] }
    }

    origin = [0,0] 

    result = SquareGetter.handle(origin, pixel_data)

    self.assertEqual(result, 'call next handler with origin pixel and pixel data')

  def test_corner_different(self):
    pixel_data = {
      0: { 0: ['XXX'], 1: ['•••'] },
      1: { 0: ['XXX'], 1: ['XXX'] }
    }

    origin = [0,0] 

    result = SquareGetter.handle(origin, pixel_data)

    self.assertEqual(result, 'call next handler with origin pixel and pixel data')

  def test_gap_corner(self):
    pixel_data = {
      0: { 0: ['XXX'],  1: ['XXX'] },
      1: { 0: ['XXX']              }
    }

    origin = [0,0] 

    result = SquareGetter.handle(origin, pixel_data)

    self.assertEqual(result, 'call next handler with origin pixel and pixel data')


  def test_other_shapes_only(self):
    pixel_data = {
      1: { 21: ['$$$'], 22: ['+++'], 23: ['@@@'] },
      2: { 21: ['XXX'], 22: ['!!!'], 23: ['&&&'] },
      3: { 21: ['XXX'], 22: ['•••'], 23: ['•••'] }
    }

    origin = [1,21] 

    result = SquareGetter.handle(origin, pixel_data)

    self.assertEqual(result, 'call next handler with origin pixel and pixel data')

# ---------------------------------------- When square exists ----------------------------------------

  def test_square(self):
    pixel_data = {
      0: { 0: ['XXX'], 1: ['XXX'] },
      1: { 0: ['XXX'], 1: ['XXX'] }
    }

    origin = [0,0] 

    result = SquareGetter.handle(origin, pixel_data)

    self.assertEqual(result, 'call pixel chomper with start and end pixels')

  def test_square_within_other_pixels(self):
    pixel_data = {
      0: { 0: ['•••'], 1: ['•••'], 2: ['•••'], 3: ['•••'], 4: ['•••'] },
      1: { 0: ['•••'], 1: ['XXX'], 2: ['XXX'], 3: ['XXX'], 4: ['•••'] },
      2: { 0: ['•••'], 1: ['XXX'], 2: ['XXX'], 3: ['XXX'], 4: ['•••'] },
      3: { 0: ['•••'], 1: ['XXX'], 2: ['XXX'], 3: ['XXX'], 4: ['•••'] },
      4: { 0: ['•••'], 1: ['•••'], 2: ['•••'], 3: ['•••'], 4: ['•••'] }
    }

    origin = [1,1] 

    result = SquareGetter.handle(origin, pixel_data)

    self.assertEqual(result, 'call pixel chomper with start and end pixels')

  def test_square_with_other_shapes(self):
    pixel_data = {
      1: { 21: ['$$$'], 22: ['+++'], 23: ['+++'] },
      2: { 21: ['•••'], 22: ['•••'], 23: ['&&&'] },
      3: { 21: ['•••'], 22: ['•••'], 23: ['&&&'] }
    }

    origin = [2,21] 

    result = SquareGetter.handle(origin, pixel_data)

    self.assertEqual(result, 'call pixel chomper with start and end pixels')

if __name__ == '__main__':
    unittest.main()

  

