import cv2

count = 0  # 定义拍照计数变量


def main():
    global count
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # 设置分辨率
    cap.set(4, 480)
    while cap.isOpened():
        ret, img = cap.read()  # 视频读入
        if not ret:
            continue
        cv2.imshow('show', img)
        key = cv2.waitKey(30) & 0xFF
        if key == ord("q"):
            break
        elif key == ord("s"):
            count = count + 1
            cv2.imwrite("./testback" + str(count) + ".jpg", img)
            print("save success!  count =", count)


if __name__ == '__main__':
    main()