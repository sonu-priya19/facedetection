import cv2 # opencv-python

haar_cascade = cv2.CascadeClassifier("haarcascade frontalface default.xml") #Loading Algorithm 
cam = cv2.VideoCapture(1) #Initializing camera id ##0.1.2 
while True: # Infinite loop
    _,img=cam.read() #Reading frame from camera
    grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Converting color image to grayscale image
    faces=haar_cascade.detectMultiScale(grayimg, 1.3,4) #Getting Coordinates
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 10)# Drawing a rectangle
        cv2.imshow("Face Detection", img) # Display the frame
        key = cv2.waitKey(10)
        print(key)
    if key==27: #Escape key to exit
        break 
cam.release() 
cv2.destroyAllWindows()

