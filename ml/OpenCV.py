import cv2 as cv

#检测函数
def face_detect_demo(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    face_detect = cv.CascadeClassifier('E:\\OpenCV\\sources\\data\\haarcascades\\haarcascade_frontalface_alt2.xml')
    face = face_detect.detectMultiScale(gray)
    for x, y, w, h in face:
        cv.rectangle(img, (x, y), (x+w, y+h), color = (0, 0, 255), thickness=2)
    cv.imshow('result', img)

cap = cv.VideoCapture(0)


#读取图像
#img = cv.imread("C:\\Users\\xyz\\Desktop\\images.jpg")
#检测
#face_detect_demo()
while True:
    flag, flame = cap.read()
    if not flag:
        break
    face_detect_demo(flame)
    if ord('q') == cv.waitKey(5):
        break

cv.destroyAllWindows()
cap.release()