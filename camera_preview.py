import cv2

count = 0
# 获取摄像头视频
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # 设置分辨率
cap.set(4, 480)
# 获取视频宽度
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# 获取视频高度
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# 文字坐标
word_x = int(frame_width / 10)
word_y = int(frame_height / 10)

while cap.isOpened():
    ret, img = cap.read()  # 视频读入
    if not ret: continue
    cv2.imshow('show', img)
    key = cv2.waitKey(30) & 0xFF
    if key == ord("q"):
        break
    elif key == ord("s"):
        count = count + 1
        cv2.imwrite("./testback" + str(count) + ".jpg", img)
        print("save success!  count =", count)

cap.release()
cv2.destroyAllWindows()