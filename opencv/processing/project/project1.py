import cv2, numpy as np

image = cv2.imread("ball3.png", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")

# 채널 나누기
b, g, r = cv2.split(image)

dst = image.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 100, param1 = 300, param2 = 30, minRadius = 80, maxRadius = 300)

colors = ['blue', 'green', 'red']
color_cnt = [0, 0, 0]


for i in circles[0]: # circles[0][0] : x, circles[0][1] : y, circles[0][2] : radius
    x = int(i[0])
    y = int(i[1])
    radius = int(i[2])

    color = (np.argmax([b[y][x], g[y][x], r[y][x]]))

    pos1 = (x-radius, y-radius)
    pos2 = (x+radius, y+radius)
    cv2.rectangle(dst, pos1, pos2, (0, 0, 0), 3)
    cv2.putText(dst, colors[color], pos1, cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 0), 5)

    color_cnt[color] += 1

for i in range(3):
    cv2.putText(dst, f'{colors[i]} : {color_cnt[i]}', (20, 20+50*(i+1)), cv2.FONT_HERSHEY_PLAIN, 3, (0, 100, 0), 5)

cv2.imshow('title1', dst)
print(color_cnt)

cv2.waitKey(0)


