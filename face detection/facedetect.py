import cv2
haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print("Error: Could not open webcam")
    exit()
while True:   
    ret, img = cam.read()  
    if not ret:
        print("Error: Failed to capture image")
        break
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.3, minNeighbors=4)

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)

    # Show the frame with detected faces
    cv2.imshow("Face Detection", img)

    # Press 'ESC' key to exit
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # 27 is the ASCII code for the ESC key
        break

# Release the webcam and close OpenCV windows
cam.release()
cv2.destroyAllWindows()
