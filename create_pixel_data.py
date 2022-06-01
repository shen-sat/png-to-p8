import cv2 as cv

class CreatePixelData:

  @staticmethod
  def create_pixel_data(image_path):
    image = cv.imread(image_path)

    pixel_data = {}
    for y, row in enumerate(image):
      for x, column in enumerate(row):
        if y in pixel_data:
          pixel_data[y][x] = [column[2],column[1],column[0]]
        else:
          pixel_data[y] = {}
          pixel_data[y][x] = [column[2],column[1],column[0]]

    return pixel_data