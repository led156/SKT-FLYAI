import numpy as np, cv2

image = cv2.imread( "images/color.jpg", cv2.IMREAD_COLOR)   # 영상 읽기
if image is None: raise Exception("영상 파일 읽기 오류 발생")   # 예외 처리


mask = np.zeros(image.shape, np.uint8)
# mask = np.zeros(image.shape[:2], np.uint8)

center = (190, 170)
size = (120, 60)
cv2.ellipse(mask, center, size, 90, 0, 360, (255, 255, 255), -1) # 타원 그리기

circle_image = cv2.bitwise_and(image, mask)
# circle_image = cv2.bitwise_and(image, image, mask = mask)


cv2.imshow("image", image) # 원본 이미지 띄우기
cv2.imshow("image2", circle_image)
cv2.waitKey(0)