# 관심 영역 지정하고, 관심 영역의 녹색 성분 증가시키기

import cv2

def put_string(frame, text, pt, value, color=(120, 200, 90)):
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)
    cv2.putText(frame, text, pt, font, 0.7, color, 2)


capture = cv2.VideoCapture(1) # 카메라 포트 연결
if capture.isOpened() == False: raise Exception("카메라 연결 안됨")

frame_rate = capture.get(cv2.CAP_PROP_FPS) # 초당 프레임 수
delay = int(1000 / frame_rate) # 지연 시간

while True:
    ret, frame = capture.read()
    if not ret: break   
    if cv2.waitKey(30) >= 0 : break

    cv2.rectangle(frame, (200, 100), (300, 300), (0, 0, 255), 3)
    blue, green, red = cv2.split(frame)

    green_rect = green[100:300, 200:300]

    cv2.add(green_rect, 50, green_rect)
    frame = cv2.merge( [blue, green, red] )                 # 단일채널 영상 합성
    
    cv2.imshow("Read Video File", frame)

capture.release()


