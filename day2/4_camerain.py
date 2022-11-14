import cv2
import sys

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('카메라를 열 수 없습니다')
    sys.exit()

print('가로 사이즈: ', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
print('가로 사이즈: ', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

while True:
    ret, frame = cap.read() # ret에는 true/false, frame에는 이미지(캠으로 한장 찍어서)가 저장

    if not ret:
        break

    inversed = ~frame # 화면 반전

    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    if cv2.waitKey(10) == 27: # ESC키를 누르면 탈출
        break



cap.release() # 캠을 꺼주고 자원(cpa)을 반납
cv2.destroyAllWindows()