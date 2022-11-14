import cv2
import sys
import glob # 이미지나 특정 파일들을 디렉토리를 찾아 한꺼번에 다 불러올 수 있음

imgs = glob.glob('images\\*jpg') # 'images' 폴더 안에 모든 jpg파일을 다 가져와서 리스트로 저장
print(imgs)

if not imgs:
    print('영상을 불러올 수 없습니다')
    sys.exit()

idx = 0

while True:
    img = cv2.imread(imgs[idx]) # 이미지 불러와서 저장

    if img is None:
        print('영상을 불러올 수 없습니다')
        break

    cv2.imshow('image', img) # 창 이름이  image, 여기에 img를 보여주기
    if cv2.waitKey(1000) >= 0: # 1초를 기다리는데, 중간에 키가 들어오면
        break

    idx += 1
    if idx >= len(imgs): # 인덱스를 다 돌았으면
        idx = 0 # 다시 처음으로 돌아가라

cv2.destroyAllWindows()