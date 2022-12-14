import cv2
import sys

src = cv2.imread('field.bmp')

if src is None:
    print('영상을 불러올 수 없습니다')
    sys.exit()

# 바꿔주는 이유: 평활화를 수행할 때 값을 뽑는 합수를 사용하기 위해
ycrcb_planes = []
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb) # 컬러들을 다른 타입으로
ycrcb_planes = cv2.split(src_ycrcb)

ycrcb_planes = list(ycrcb_planes)

# 밝기 성분에 대해서만 히스토그램 평활화 수행
ycrcb_planes[0] = cv2.equalizeHist(ycrcb_planes[0]) # 평활화 수행해서 다시 저장

dst_ycrcb = cv2.merge(ycrcb_planes)
dst = cv2.cvtColor(dst_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()