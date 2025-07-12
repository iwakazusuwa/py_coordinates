import cv2

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, y)

img = cv2.imread('aa.png')
cv2.imshow('aa', img)
cv2.setMouseCallback('aa', onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()