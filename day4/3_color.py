import cv2
import sys

src = cv2.imread('candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('영상을 불러올 수 업습니다')
    sys.exit()

print('src.shape : ', src.shape) # (480, 640, 3)
print('src.dtype : ', src.dtype) # uint8

b_plane, g_plane, r_plane = cv2.split(src)

# b_plane = src[:, :, 0]
# b_plane = src[:, :, 1]
# b_plane = src[:, :, 2]

cv2.imshow('src', src)
cv2.imshow('b_plane', b_plane) # 채널을 하나씩 가져왔기 때문에 밝기로만 나타남
cv2.imshow('g_plane', g_plane)
cv2.waitKey()
cv2.destroyAllWindows()