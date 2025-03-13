import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')#contains data to detect faces

# function to do the whole detection process
def detect():
    cap = cv2.VideoCapture(0)#capture video from camera
    
    while True:
        img = cap.read()[1]#read the video
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #convert the image to gray scale
        
        face = face_cascade.detectMultiScale(gray, 1.1, 4)#detect faces in the image
        for(x, y, w, h) in face:
            cv2.rectangle(img, (x, y), (x+y, y+h),(100,255,50), 2)#draw rectangle around the face
            
        cv2.imshow('img', img)#display the image
        if cv2.waitKey(1)==27: #Exits immediately esc key is presses
            break
    cap.release()
    cv2.destroyAllWindows()
detect()