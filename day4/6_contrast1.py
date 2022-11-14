import cv2
import sys
import numpy as np

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('영상을 읽을 수 없습니다')
    sys.exit()

alpha = 1.0

# 하는 이유: 명암비를 만져주면서 잘 안 보이던 부분은 잘 보이게, 너무 밝은 부분은 낮춰서 더 잘 보이도록 하기 위해서
dst = np.clip((1+alpha)*src - 128*alpha, 0, 255).astype(np.uint8) # 하한값:0, 상한값: 255

cv2.imshow('src', src)
cv2.imshow('des', dst)
cv2.waitKey()

cv2.destroyAllWindows()