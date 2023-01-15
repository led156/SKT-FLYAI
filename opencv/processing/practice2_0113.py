import time, cv2, numpy as np
from Common.utils import print_matInfo

# 파일 리드
gray_image = cv2.imread("images/mine2.jpg", cv2.IMREAD_GRAYSCALE)
if gray_image is None: raise Exception("영상파일 읽기 에러")

(x, y), (w, h) = (10, 20), (15, 15)

roi = gray_image[x:x+w, y:y+h]

cv2.rectangle(gray_image, (x, y), (x+w, y+h), 255, 1)
# cv2.rectangle(gray_image, (x, y, w, h), 255, 1)

for row in roi:
    for ele in row:
        print(ele, end = ' ')
    print()

cv2.imshow('image', gray_image)
cv2.waitKey(0)