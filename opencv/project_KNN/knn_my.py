import cv2
import numpy as np
from matplotlib import pyplot as plt
import math

k = 3

# 데이터 뿌릴 위치 설정
dataPos = np.random.randint(0., 100., (25, 2))
# 데이터의 색상 값 설정
dataColor = np.random.randint(0., 2., (25, 1))

# 데이터 뿌리기
# (1) Red
red = dataPos[dataColor.ravel() == 0]
plt.scatter(red[:, 0], red[:, 1], 80, 'r', 's')
# (2) Blue
blue = dataPos[dataColor.ravel() == 1]
plt.scatter(blue[:, 0], blue[:, 1], 80, 'b', 'o')


# 비교할 데이터 추가
new_data = np.random.randint(0, 100, (1, 2)).astype(np.float32)
plt.scatter(new_data[:, 0], new_data[:, 1], 80, 'y', '*')


# 거리 계산
dist_list = [] # (거리, 색깔idx)
for i in range(len(dataPos)):
    dist = math.pow(dataPos[i, 0] - new_data[:, 0], 2) + math.pow(dataPos[i, 1] - new_data[:, 1], 2)
    dist_list.append((dist, int(dataColor[i, 0])))

# 거리 순서로 정렬
dist_list = sorted(dist_list, key=lambda dist_: dist_[0])   # sort by age
print('dist_list : ', dist_list)

color = np.array([0, 0])
for i in range(k):
    color[dist_list[i][1]] += 1
print('color array : ', color)

color_name = ['red', 'blue']
print('Result : ', color_name[color.argmax()])

plt.show()
