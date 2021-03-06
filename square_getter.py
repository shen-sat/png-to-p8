# Looks for a square made up of the same-color pixels, 
# using the origin pixel as a starting point
class SquareGetter:

	@classmethod
	def handle(self, origin, pixel_data):
		corner = self.corner(origin, pixel_data)

		if corner and self.is_square(origin, corner, pixel_data):
			return 'call pixel chomper with start and end pixels'
		else:
			return 'call next handler with origin pixel and pixel data'
			
	@classmethod
	def corner(self, y_x, pixel_data, is_origin=True):
	  y, x, color = self.__pixel(y_x, pixel_data)

	  try:
	    pixel_data[y + 1][x + 1]
	  except KeyError:
	    if is_origin:
	      return None
	    else:
	      return [y, x]
	  
	  if pixel_data[y + 1][x + 1] == color:
	    return self.corner([y + 1, x + 1], pixel_data, False)
	  else:
	    if is_origin:
	      return None
	    else:
	      return [y, x] 

	@classmethod
	def is_square(self, origin, corner, pixel_data):
	  min_y, min_x, origin_color = self.__pixel(origin, pixel_data)

	  max_y = corner[0]
	  max_x = corner[1]

	  for y in range(min_y, max_y + 1):
	    for x in range(min_x, max_x + 1):
	      try:
	        pixel_data[y][x]
	      except KeyError:
	        return False

	      if pixel_data[y][x] != origin_color:
	      	return False

	    return True

	@staticmethod
	def __pixel(y_x, pixel_data):
		y = y_x[0]
		x = y_x[1]
		color = pixel_data[y][x]

		return y, x, color