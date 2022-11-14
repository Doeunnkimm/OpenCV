import cv2
import sys

src = cv2.imread('cat.bmp')

if src is None:
    print('영상을 불러올 수 없습니다')
    sys.exit()

# ractangle tuple
rc = (250, 120, 200, 200) # 사각형으로 좌표 잡아주는

cpy = src.copy()
cv2.rectangle(cpy, rc, (0, 0, 255), 2)
cv2.imshow('src', cpy)
cv2.waitKey()

for i in range(1, 4):
    src = cv2.pyrDown(src)
    cpy = src.copy()
    cv2.rectangle(cpy, rc, (0, 0, 255), 2, shift=i)
    cv2.imshow('src', cpy)
    cv2.waitKey() # 키를 누를 때까지 멈춰있음
    cv2.destroyWindow('src')

cv2.destroyAllWindows()