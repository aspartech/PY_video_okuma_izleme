import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
filename = "C:\mrb\webcam.avi"
codec = cv2.VideoWriter_fourcc("W", "M", "V", "2")
frameRate = 30
resolution = (640, 480)
videoFileOutput = cv2.VideoWriter(filename, codec, frameRate, resolution)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    videoFileOutput.write(frame)
    if ret == 0:
        break
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
videoFileOutput.release()
cap.release()
cv2.destroyAllWindows()
