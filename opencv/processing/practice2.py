# 좌우반전 해결하기

import cv2

fps = 15                                       # 초당 프레임 수
delay = round(1000/ fps)                            # 프레임 간 지연 시간
size  = (600, 480)                                  # 동영상 파일 해상도
fourcc = cv2.VideoWriter_fourcc(*'mp4v')            # 압축 코덱 설정

capture = cv2.VideoCapture(1) # 카메라 포트 연결
if capture.isOpened() == False: raise Exception("카메라 연결 안됨")

capture.set(cv2.CAP_PROP_ZOOM, 1)                   # 카메라 속성 지정
capture.set(cv2.CAP_PROP_FOCUS, 0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH , size[0])     	# 해상도 설정
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, size[1])

writer = cv2.VideoWriter("images/Flip_test.mov", fourcc, fps, size)
if writer.isOpened() == False: raise Exception("동영상 파일 개방 안됨")

while True:
    ret, frame = capture.read()
    if not ret: break   
    if cv2.waitKey(30) >= 0 : break

    frame = cv2.flip(frame, 1)
    '''
     0 means flipping around the x-axis and positive value (for example, 1) means flipping around y-axis. 
     Negative value (for example, -1) means flipping around both axes. Return Value: It returns an image.
    '''
    writer.write(frame)

    cv2.imshow("Write (Flip) Video File", frame)

capture.release()


