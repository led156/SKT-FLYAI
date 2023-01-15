import cv2, numpy as np
from Common.utils import print_matInfo

# 파일 리드
gray_image = cv2.imread("images/read_color.jpg", cv2.IMREAD_GRAYSCALE)
color_image = cv2.imread("images/read_color.jpg", cv2.IMREAD_COLOR)

if gray_image is None or color_image is None:
    raise Exception("영상파일 읽기 에러")

# 1-1
_, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

# 1-2
binary_image_np = np.ndarray(gray_image.shape)

for i in range(gray_image.shape[0]):
    for j in range(gray_image.shape[1]):
        if gray_image[i][j] < 128:
            binary_image_np[i][j] = 0
        else:
            binary_image_np[i][j] = 255


# 2
blue, green, red = cv2.split(color_image)

_, b_binary_image = cv2.threshold(blue, 128, 255, cv2.THRESH_BINARY)
_, g_binary_image = cv2.threshold(green, 128, 255, cv2.THRESH_BINARY)
_, r_binary_image = cv2.threshold(red, 128, 255, cv2.THRESH_BINARY)

# 츌력
cv2.imshow('grayImage', gray_image)
cv2.imshow('binaryImage_opencv', binary_image)
cv2.imshow('binaryImage_np', binary_image_np)

cv2.imshow('colorImage', color_image)
cv2.imshow('blueBinaryImage', b_binary_image)
cv2.imshow('greenBinaryImage', g_binary_image)
cv2.imshow('redBinaryImage', r_binary_image)

cv2.waitKey(0)