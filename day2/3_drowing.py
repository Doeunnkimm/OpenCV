import cv2
import numpy as np

img = np.full((400, 400, 3), 255, np.uint8) # fill..? 400x400의 컬러 채널 생성

cv2.line(img, (50, 50), (200, 50), (0, 0, 225), 5)

cv2.rectangle(img, (40, 200, 150, 100), (0, 255, 0), 2)
cv2.rectangle(img, (70, 220, 150, 100), (0, 120, 0), -1)

cv2.circle(img, (300, 100), 50, (255, 255, 0), -1)

text = 'Hello, Python'
cv2.putText(img, text, (50, 350), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255))
cv2.imshow('img', img)
cv2.waitKey()
cv2.destroyAllWindows()