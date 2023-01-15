import cv2

capture = cv2.VideoCapture("video.mp4")
w = round(capture.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer = cv2.VideoWriter('output.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 30.0, (w, h))

while True:
    _, frame = capture.read()

    if frame is None:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    avg_value = cv2.mean(gray)[0] # 영상 픽셀의 평균값

    if avg_value < 50: # 평균값이 100보다 작다면 영상을 밝게
        alpha = 1.25
        beta = 25
        frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)
    elif avg_value > 200: # 평균값이 200보다 크다면 영상을 어둡게
        alpha = 0.75
        beta = -25
        frame = cv2.convertScaleAbs(frame, alpha=alpha, beta=beta)

    cv2.imshow("Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()