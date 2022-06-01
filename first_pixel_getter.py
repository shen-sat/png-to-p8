# Looks for the first pixel in a given set of pixel data
class EmptyPixelDataException(Exception):
	pass

class FirstPixelGetter:

	@staticmethod
	def handle(pixel_data):

		for y in pixel_data:
			if pixel_data[y] == {}:
				continue
			else:
				for x in pixel_data[y]:
					return [y, x]

		raise EmptyPixelDataException



