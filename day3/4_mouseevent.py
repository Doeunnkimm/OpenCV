import cv2
import numpy as np

oldx = oldy = -1 # 아예 없는 값으로 저장. 전역 변수

def on_mouse(event, x, y, flags, param):
    global oldx, oldy # 전역변수를 사용할 수 있도록 설정. 지정

    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽버튼이 눌렀다면
        oldx, oldy = x, y # 누른 지점의 x, y 값을 가져와서 저장
        print('왼쪽 버튼 클릭 : %d, %d' % (x, y))
    elif event == cv2.EVENT_LBUTTONUP: # 마우스 왼쪽 버튼을 뗐다면
        print('왼쪽 버튼 뗌 : %d, %d' % (x, y))
    elif event == cv2.EVENT_MOUSEMOVE: # 마우스 커서가 움직였다면
        if flags & cv2.EVENT_FLAG_LBUTTON: # flag가 true는 마우스가 눌려져있다는 의미.즉 왼쪽 버튼이 눌러져 있는 상태라면
            cv2.line(img, (oldx, oldy), (x, y), (255, 51, 255), 3,  cv2.LINE_AA) # 클릭 해서 뗀 좌표까지 라인을 그어달라는 의미
            cv2.imshow('image', img)
            oldx, oldy = x, y

img = np.ones((480, 640, 3), dtype=np.uint8) * 255 # 검정색화면 * 255 = 하얀색 화면

cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse, img) # 마우스 이벤트가 발생하면 자동으로 on_mouse 함수가 실행

cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()

