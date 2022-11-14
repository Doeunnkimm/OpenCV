import cv2
import sys

import numpy as np

cap1 = cv2.VideoCapture('Lake.mp4')
cap2 = cv2.VideoCapture('puma.mp4')

if not cap1.isOpened() or not cap2.isOpened():
    print('비디오를 열 수 없습니다')
    sys.exit()

frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT)) # 237
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT)) # 324
fps = cap1.get(cv2.CAP_PROP_FPS) # 30
eff_frames = int(fps * 2) # 30 * 2 = 60

print('frame_cnt1: ', frame_cnt1)
print('frame_cnt2: ', frame_cnt2)
print('fps: ', fps)

delay = int(1000 / fps)

w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'DIVX')

out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

# 1번 동영상 마지막 2초전까지만 복사
for i in range(frame_cnt1 - eff_frames): # 237 - 60 : 2초 전까지
    ret1, frame1 = cap1.read()

    out.write(frame1) # 읽은 것을 쓰는 중. release해야 끝나늑 것
    cv2.imshow('output', frame1)
    cv2.waitKey(delay)

# 1번 동영상 마지막 2초와 2번 동영상 시작 2초
for i in range(eff_frames):
    ret1, frame1 = cap1.read() # 남은 60프레임
    ret2, frame2 = cap2.read() # 처음 60프레임

    dx = int(w / eff_frames) * i # (1280 / 60) * i

    frame = np.zeros((h, w, 3), dtype=np.uint8) # 검정색 화면
    # for문을 돌면서 검정색 화면에 frame1과 frame2의 화면을 조절하면서 넣기
    frame[:, 0:dx, :] = frame2[:, 0:dx, :]
    frame[:, dx:w, :] = frame1[:, dx:w, :] # w = 1280

    out.write(frame)
    cv2.imshow('output', frame)
    cv2.waitKey(delay)

for i in range(eff_frames, frame_cnt2):
    ret2, frame2 = cap2.read()

    out.write(frame2)
    cv2.imshow('output', frame2)
    cv2.waitKey(delay)

cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()

