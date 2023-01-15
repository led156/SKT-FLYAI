import time, cv2, numpy as np
from Common.utils import print_matInfo

def time_check(func, msg, image):
    start_time = time.perf_counter()
    ret_img = func(image)
    elapsed = (time.perf_counter() - start_time) * 1000
    print(msg, "수행시간 : %0.2f ms" % elapsed)
    return ret_img

def mat_access1(mat):
    nmat = np.ndarray(mat.shape)
    for i in range(nmat.shape[0]):
        for j in range(nmat.shape[1]):
            k = mat[i, j]
            nmat[i, j] = 255 - k
    return nmat.astype('uint8')

def mat_access2(mat):
    nmat = np.ndarray(mat.shape)
    for i in range(nmat.shape[0]):
        for j in range(nmat.shape[1]):
            k = mat.item(i, j)
            nmat.itemset((i, j), 255 - k)
    return nmat.astype('uint8')

def mat_access3(mat):
    lut = [255 - i for i in range(256)]
    lut = np.array(lut, np.uint8)
    nmat = lut[mat]
    return nmat

def mat_access4(mat):
    namt = cv2.subtract(255, mat)
    return namt

def mat_access5(mat):
    namt = 255 - mat
    return namt

# 파일 리드
gray_image = cv2.imread("images/mine2.jpg", cv2.IMREAD_GRAYSCALE)

if gray_image is None: raise Exception("영상파일 읽기 에러")


# 오리지날
cv2.imshow('원본', gray_image)

# 반전1 : 직접 접근 - 가장 cost 가 큼.
gray_image1 = time_check(mat_access1, "[방법1] 직접 접근", gray_image)
# gray_image1 = mat_access1(gray_image)
cv2.imshow('반전1', gray_image1)

# 반전2 : item()
gray_image2 = time_check(mat_access2, "[방법2] item() 함수", gray_image)
# gray_image2 = mat_access2(gray_image)
# cv2.imshow('반전2', gray_image2)

# 반전3 : 룩업테이블
gray_image3 = time_check(mat_access3, "[방법3] 룩업테이블", gray_image)
# cv2.imshow('반전3', gray_image3)

# 반전4 : opencv 함수
gray_image4 = time_check(mat_access4, "[방법4] OpenCV", gray_image)

# 반전5 : ndarray 산술 연산 방법
gray_image5 = time_check(mat_access5, "[방법5] ndarray", gray_image)

cv2.waitKey(0)