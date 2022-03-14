import cv2

path = "/Users/trivikram/Desktop/HaarCascades/cascade.xml"
cameraNo = 0
objectName = 'FACE'
frameWidth = 640
frameHeight = 480
color = (255, 0, 255)


cap = cv2.VideoCapture(cameraNo)
if not cap.isOpened():
    raise IOError("Cannot open webcam")

cap.set(3, frameWidth)
cap.set(4, frameHeight)

def empty(a):
    pass

# CREATE TRACKBAR; PURELY FOR TESTING PURPOSES
cv2.namedWindow("TRACKBAR")
cv2.resizeWindow("TRACKBAR", frameWidth, frameHeight+100 )
cv2.createTrackbar("Scale", " TRACKBAR", 400, 1000, empty)
cv2.createTrackbar("Neig", "TRACKBAR", 8, 20, empty)
cv2.createTrackbar("Min Area", "TRACKBAR", 0, 100000, empty)

cascade = cv2.CascadeClassifier(path)

while True:
    cameraBrightness = cv2.getTrackbarPos("Brightness", "TRACKBAR")
    cap.set(10, cameraBrightness)
    success, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    scaleVal = 1 + (cv2.getTrackbarPos("Scale", "TRACKBAR") / 1000)
    neig = cv2.getTrackbarPos("Neig", "TRACKBAR")
    #objects = cascade.detectMultiScale(gray, scaleVal, neig)
    objects = cascade.detectMultiScale(gray)

    for (x, y, w, h) in objects:
        area = w*h
        minArea = cv2.getTrackbarPos("Min Area", "TRACKBAR")
        if area > minArea:
            cv2.rectangle(img, (x, y), (x+w, y+h), color, 3)
            cv2.putText(img, objectName, (x, y-5), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, color, 2)
            roi_color = img[y:y+h, x:x+w]

    cv2.imshow("TRACKBAR", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
















