import cv2
import sys
import numpy as np

src = cv2.imread('tekapo.bmp')

if src is None:
    print('영상을 불러올 수 없습니다')
    sys.exit()

# 변환 행렬
aff = np.array([[1, 0, 200], [0, 1, 100]], dtype=np.float32) # a : x축으로 이동하고 싶은 만큼, b: y축으로 이동하고 싶은 만큼

dst = cv2.warpAffine(src, aff, (0, 0))

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()