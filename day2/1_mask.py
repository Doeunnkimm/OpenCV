import cv2
import sys

src = cv2.imread('airplane.bmp')
mask = cv2.imread('mask_plane.bmp', cv2.IMREAD_GRAYSCALE) # 흑백 영상으로 불러옴
dst = cv2.imread('field.bmp')

if src is None or mask is None or dst is None:
    print('영상을 불러올 수 없습니다')
    sys.exit()

# cv2.copyTo() 함수를 사용하기 위해서는...
# scr, mask, dst는 모두 크기가 같아야 함
# src와 dst는 같은 타입이어야 하며, mask는 반드시 그레이스케일 타입의 이진 영상
cv2.copyTo(src, mask, dst)

cv2.imshow('src', src)
cv2.imshow('mask', mask)
cv2.imshow('dst', dst)

cv2.waitKey()
cv2.destroyAllWindows()