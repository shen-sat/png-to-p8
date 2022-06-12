import cv2 as cv

class ColorIndexList:

  @classmethod
  def create(self, image_path):
    image = cv.imread(image_path)

    color_index_list = []
    for y, row in enumerate(image):
      for x, column in enumerate(row):
        rgb = [ column[2],column[1],column[0] ]
        color_index = self.__pico8_color_index(rgb)
        color_index_list.append(color_index)
        # if y in pixel_data:
        #   pixel_data[y][x] = [column[2],column[1],column[0]]
        # else:
        #   pixel_data[y] = {}
        #   pixel_data[y][x] = [column[2],column[1],column[0]]

    return color_index_list

  @staticmethod
  def __pico8_color_index(rgb):
    my_map = {
      # black
      str([0, 0, 0]) : 0,
      # dark-blue
      str([29, 43, 83]) : 1,
      # dark-purple
      str([126, 37, 83]) : 2,
      # dark-green
      str([0, 135, 81]) : 3,
      # brown
      str([171, 82, 54]) : 4,
      # dark-grey
      str([95, 87, 79]) : 5,
      # light-grey
      str([194, 195, 199]) : 6,
      # white
      str([255, 241, 232]) : 7,
      # red
      str([255, 0, 77]) : 8,
      # orange
      str([255, 163, 0]) : 9,
      # yellow
      str([255, 236, 39]) : 10,
      # green
      str([0, 228, 54]) : 11,
      # blue
      str([41, 173, 255]) : 12,
      # lavender
      str([131, 118, 156]) : 13,
      # pink
      str([255, 119, 168]) : 14,
      # light-peach
      str([255, 204, 170]) : 15
    }

    return my_map[str(rgb)]