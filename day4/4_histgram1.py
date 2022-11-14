import cv2
import sys
import matplotlib.pyplot as plt

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('영상을 읽어올 수 없습니다')
    sys.exit()

# img가 하나여서 channal도 하나. 즉 인덱스 0으로
hist = cv2.calcHist([src], [0], None, [256], [0, 256])

cv2.imshow('src', src)
# 각각 밝기에 해당하는 픽셀의 갯수를 히스토그램으로 출력
plt.plot(hist)
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()