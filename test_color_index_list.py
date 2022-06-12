import unittest
from color_index_list import ColorIndexList

class Create(unittest.TestCase):

  def test_1x1_red(self):
    result = ColorIndexList.create('1x1-red.png')
    expected_result = [ 
      8 
    ]

    self.assertEqual(result, expected_result)

  def test_2x2_red(self):
    result = ColorIndexList.create('2x2-red.png')    
    expected_result = [
      8,  8,
      8,  8
    ]

    self.assertEqual(result, expected_result)

  def test_2x2_red_red_blue_blue(self):
    result = ColorIndexList.create('2x2-red-red-blue-blue.png')    
    expected_result = [
      8,  8,
      12, 12
    ]
    self.assertEqual(result, expected_result)

  def test_2x2_red_blue_red_blue(self):
    result = ColorIndexList.create('2x2-red-blue-red-blue.png')
    
    expected_result = [
      8,  12,
      8,  12
    ]
    self.assertEqual(result, expected_result)

  def test_2x2_red_blue_green_yellow(self):
    result = ColorIndexList.create('2x2-red-blue-green-yellow.png')
    
    expected_result = [
      8,  12,
      11, 10
    ]
    self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()

  

