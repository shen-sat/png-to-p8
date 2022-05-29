# contract:
# - pixel_data can be made up of:
# 	- pixels eg
# 		{
# 			0: {}, 
# 			1: { 1: [1,1,[color]] }
# 		}
# 	- a hash of empty rows, eg 
# 		{
# 			0: {}, 
# 			1: {}
# 		}
class GetFirstPixel:
	
	@staticmethod
	def handle(pixel_data, output):
		for y in pixel_data:
			if pixel_data[y] == {}:
				continue
			else:
				for x in pixel_data[y]:
					return pixel_data[y][x]

		return 'all pixel data processed'



