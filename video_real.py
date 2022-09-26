import cv2, time

video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
frames = 1
while True:
    frames += 1
    check, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Capturing", gray)
    key = cv2.waitKey(50)
    if key == ord('q'):
        break

print(frames)
video.release()
cv2.destroyAllWindows()