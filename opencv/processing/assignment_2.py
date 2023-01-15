import cv2, numpy as np
from Common.utils import print_matInfo

def compute_otsu_criteria(im, th):
    # create the thresholded image
    thresholded_im = np.zeros(im.shape)
    thresholded_im[im >= th] = 1

    # compute weights
    nb_pixels = im.size
    nb_pixels1 = np.count_nonzero(thresholded_im)
    weight1 = nb_pixels1 / nb_pixels
    weight0 = 1 - weight1

    # if one the classes is empty, eg all pixels are below or above the threshold, that threshold will not be considered
    # in the search for the best threshold
    if weight1 == 0 or weight0 == 0:
        return np.inf

    # find all pixels belonging to each class
    val_pixels1 = im[thresholded_im == 1]
    val_pixels0 = im[thresholded_im == 0]

    # compute variance of these classes
    var0 = np.var(val_pixels0) if len(val_pixels0) > 0 else 0
    var1 = np.var(val_pixels1) if len(val_pixels1) > 0 else 0

    return weight0 * var0 + weight1 * var1


# 파일 리드
gray_image = cv2.imread("images/Lenna.png", cv2.IMREAD_GRAYSCALE)
if gray_image is None:
    raise Exception("영상파일 읽기 에러")
cv2.imshow('grayImage', gray_image)

# 전처리
min_val, max_val, _, _ = cv2.minMaxLoc(gray_image)
ratio = 255 / (max_val - min_val)
gray_image = np.round((gray_image - min_val) * ratio).astype('uint8')

# [방법 1-1]
_, binary_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


# [방법 1-2]
threshold_range = range(np.max(gray_image)+1) # 범위값을 담는 array
criterias = [compute_otsu_criteria(gray_image, th) for th in threshold_range] # 범위값에 대한 
best_threshold = threshold_range[np.argmin(criterias)]


binary_image_np = np.ndarray(gray_image.shape)

for i in range(gray_image.shape[0]):
    for j in range(gray_image.shape[1]):
        if gray_image[i][j] < best_threshold:
            binary_image_np[i][j] = 0
        else:
            binary_image_np[i][j] = 255


# 출력
cv2.imshow('binaryImage_opencv', binary_image)
cv2.imshow('binaryImage_np', binary_image_np)


cv2.waitKey(0)