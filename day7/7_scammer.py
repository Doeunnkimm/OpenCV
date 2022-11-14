import cv2
import sys
import numpy as np

def drawROI(img, corners):
    cpy = img.copy()
    c1 = (192, 192, 255)
    c2 = (128, 128, 255)

    for pt in corners:
        # 25: 반지름, c1: 색상, -1: 내부 채우기
        cv2.circle(cpy, tuple(pt.astype(int)), 25, c1, -1, cv2.LINE_AA)
    # 시작 좌표랑 끝 좌표를 선으로 그려줌. 2: 선굵기
    cv2.line(cpy, tuple(corners[0].astype(int)), tuple(corners[1].astype(int)), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[1].astype(int)), tuple(corners[2].astype(int)), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[2].astype(int)), tuple(corners[3].astype(int)), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[3].astype(int)), tuple(corners[0].astype(int)), c2, 2, cv2.LINE_AA)

    return cpy

def onMouse(event, x, y, flags, param):
    global srcQuad, dragSrc, ptOld, src

    if event == cv2.EVENT_LBUTTONDOWN: # 마우스 왼쪽 버튼이 눌렀다면
        for i in range(4):
            if cv2.norm(srcQuad[i] - (x, y)) < 25: # 원 안에 찝혔다면
                dragSrc[i] = True
                ptOld = (x, y)
                break

    if event == cv2.EVENT_LBUTTONUP:
        for i in range(4):
            dragSrc[i] = False

    if event == cv2.EVENT_MOUSEMOVE: # 마우스가 움직이고 있을 때
        for i in range(4):
            if dragSrc[i]: # 지금 True인 점만 들어가게 됨
                dx = x - ptOld[0]
                dy = y - ptOld[1]

                srcQuad[i] += (dx, dy)
                cpy = drawROI(src, srcQuad)
                cv2.imshow('img', cpy)
                ptOld = (x, y)
                break


src = cv2.imread('scanned.jpg')

if src is None:
    print('영상을 불러올 수 없습니다')
    sys.exit()

h, w = src.shape[:2]
dw = 500
# A4용지 크기: 210*297cm
dh = round(dw * 297 / 210)

srcQuad = np.array([[30, 30], [30, h-30], [w-30, h-30], [w-30, 30]], np.float32)
dstQuad = np.array([[0, 0], [0, dh], [dw, dh], [dw, 0]], np.float32)
dragSrc = [False, False, False, False]

disp = drawROI(src, srcQuad)


cv2.imshow('img', disp)
# 마우스 이벤트
cv2.setMouseCallback('img', onMouse) #img에 마우스 이벤트가 발생하면 onMouse 함수를 호출
cv2.waitKey()

while True:
    key = cv2.waitKey()
    if key == 13: # 엔터키
        break
    elif key == 27: # ESC키
        cv2.destroyWindows('img')
        sys.exit()

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
dst = cv2.warpPerspective(src, pers, (dw, dh), flags=cv2.INTER_CUBIC)

cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()