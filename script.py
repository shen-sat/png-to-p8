import cv2 as cv

image = cv.imread('2x2-red-blue-green-yellow.png')


# print(image[0,2])

result = {}
for y_index, row in enumerate(image):
  y = y_index
  for x_index, column in enumerate(row):
    x = x_index
    if x in result:
      result[x][y] = [column[2],column[1],column[0]]
    else:
      result[x] = {}
      result[x][y] = [column[2],column[1],column[0]]
    # print(f'x:{x} y:{y}')





for key in result:
  print(f'{key} => {result[key]}')

# print(result[0][0])
# print(result[1][0])
# print(result[0][1])
# print(result[1][1])







# ------

# hash = {
# 	0 => { 1 => [255,255,255] }
# }

# result[0][1]

