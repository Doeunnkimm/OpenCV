import cv2

img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', img)

while True:
    keyvalue = cv2.waitKey() # 키 값을 누르면 그 키 값이 변수에 들어가게 됨
    if keyvalue == ord('i') or keyvalue == ord('I'): # ord: 아스키코드 뽑아내는 함수
        img = ~img
        cv2.imshow('image', img)
    elif keyvalue == 27:
        break

cv2.destroyAllWindows()