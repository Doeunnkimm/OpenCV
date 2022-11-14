import cv2
import sys
import math
import numpy as np

src = cv2.imread('tekapo.bmp')

if src is None:
    print('영상을 불러올 수 없습니다')
    sys.exit()

# center position : 원본 사진을 가지고 중심 좌표 찾음
cp = (src.shape[1] / 2, src.shape[0] / 2) # shape[1]: height, shape[0]: width
rot = cv2.getRotationMatrix2D(cp, 20, 0.5)

dst = cv2.warpAffine(src, rot, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()