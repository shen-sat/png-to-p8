# Looks for a square made up of the same-color pixels, 
# using the origin pixel as a starting point
class SquareGetter:

	@classmethod
	def handle(self, origin_pixel, pixel_data):
	
		corner_pixel = self.corner_pixel(origin_pixel, pixel_data)

		if corner_pixel and self.is_square(origin_pixel, corner_pixel, pixel_data):
			return 'call pixel chomper with start and end pixels'
		else:
			return 'call next handler with origin pixel and pixel data'
			
	@classmethod
	def corner_pixel(self, pixel, pixel_data, is_origin_pixel=True):
	  y = pixel[0]
	  x = pixel[1]
	  color = pixel[2]

	  try:
	    corner_pixel = pixel_data[y + 1][x + 1]
	  except KeyError:
	    if is_origin_pixel:
	      return None
	    else:
	      return pixel
	  
	  if corner_pixel[2] == color:
	    return self.corner_pixel(corner_pixel, pixel_data, False)
	  else:
	    if is_origin_pixel:
	      return None
	    else:
	      return pixel 

	@staticmethod
	def is_square(origin_pixel, corner_pixel, pixel_data):
	  min_y = origin_pixel[0]
	  min_x = origin_pixel[1]
	  color = origin_pixel[2]

	  max_y = corner_pixel[0]
	  max_x = corner_pixel[1]

	  for y in range(min_y, max_y + 1):
	    for x in range(min_x, max_x + 1):
	      try:
	        pixel = pixel_data[y][x]
	      except KeyError:
	        return False

	      if pixel == origin_pixel:
	        continue
	      elif pixel == corner_pixel:
	        return True
	      else:
	        if pixel[2] != color:
	          return False