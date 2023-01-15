import cv2

image = cv2.imread("images/read_color.jpg", cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상파일 읽기 에러")

params_jpg = (cv2.IMWRITE_JPEG_QUALITY, 10) # JPEG 화질 설정 : 숫자가 작을수록 더 열화됨
params_png = [cv2.IMWRITE_PNG_COMPRESSION, 9] # PNG 압축 레벨 설정 : 숫자가 커질수록 더 압축이 잘됨 -> 보다 용량이 작아짐

cv2.imwrite("images/write_test1.jpg", image)
cv2.imwrite("images/write_test2.jpg", image, params_jpg)
cv2.imwrite("images/write_test3.png", image, params_png)
cv2.imwrite("images/write_test4.bmp", image)
print("저장 완료")