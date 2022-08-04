import cv2
from cv2 import VideoCapture
# video dosyası
## cap = cv2.VideoCapture("antalya.mp4")

# webcam

cap: VideoCapture = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    ret, frame = cap.read()

    if ret == 0:
        break

    # webcam
    frame = cv2.flip(frame, 1)

    cv2.imshow("Webcam", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()