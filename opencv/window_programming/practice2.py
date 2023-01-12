# 마우스 클릭하여 시작점과 끝점을 설정하여 사각형, 라인 그리기

import numpy as np
import cv2

def onMouse(event, x, y, flags, param):
    global cnt, pt2, pt1
    
    if event == cv2.EVENT_LBUTTONDOWN :
        if cnt == 0 :
            pt1 = (x, y)
            print(f'click 1, ({x}, {y})')
        elif cnt == 1 :
            pt2 = (x, y)
            print(f'click 2, ({x}, {y})')

            cv2.rectangle(image, pt1, pt2, red, 3, cv2.LINE_4) # 사각형 그리기
            cv2.line(image, pt1, pt2, blue) # 직선 그리기
            cv2.imshow(title, image)
        cnt = cnt + 1


orange, blue, white, red = (0, 165, 255), (255, 0, 0), (255, 255, 255), (0, 0, 255)
image = np.full((300, 700, 3), white, np.uint8) 

cnt = 0
pt1, pt2 = (0, 0), (0, 0)
title = 'title1'

cv2.imshow(title, image)

cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)