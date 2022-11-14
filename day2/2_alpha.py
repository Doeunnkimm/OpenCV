import cv2
import sys

src = cv2.imread('field.bmp')
hero = cv2.imread('hero.png', cv2.IMREAD_UNCHANGED) # png 영상

if src is None or hero is None:
    print('영상을 불러올 수 업습니다')
    sys.exit()

mask = hero[:, :, 3] # 컬러 영상
# png는 4채널. b, g, r, alpha
hero = hero[:, :, :-1] # hero는 b, g, r 3채널 (alpha 값 빼고 가져옴)
h, w = mask.shape[:2]
crop = src[10:10+h, 10:10+w] # crop은 위치를 의미

cv2.copyTo(hero, mask, crop)

cv2.imshow('src', src)
cv2.imshow('mask', mask) # mask는 이진 영상이어야 함
cv2.imshow('hero', hero)
cv2.waitKey()
cv2.destroyAllWindows()