import numpy as np
import math
import cv2
import sys
pic_name = sys.argv[1]
bm = cv2.imread(pic_name)
height, width = bm.shape[:2]
PI = math.pi
l = width // 2
new_height = l
new_width = 4 * l
new_bm = np.zeros((new_width, new_height,3))
for i in range(new_height):
    for j in range(new_width):
        radius = float(l-i)
        theta = 2.0 * PI * float(-j) / float(4.0 * l)

        fTrueX = radius * math.cos(theta)
        fTrueY = radius * math.sin(theta)

        x = int(round(fTrueX)) + l
        y = l - int(round(fTrueY))
        if (x >= 0 and x < (2*l) and y >= 0 and y < (2*l)):
            tmp_pixel = bm[x][y]
            new_bm[j][i] = tmp_pixel


new_bm = new_bm.astype(np.uint8)
new_bm = cv2.transpose(new_bm)
new_bm = cv2.flip(new_bm, 1)
cv2.imwrite('defish.jpg',new_bm)
cv2.waitKey(0)
