import cv2

#this captures video from your webcam and uses camera index usually 0
imgcapture = cv2.VideoCapture(0)

#Check if cam has opened successfully
if not imgcapture.isOpened():
    print(f"Error: Could not open camera")
    exit()
    
#function to capture, save and read an image
while(True):
    ret, frame= imgcapture.read()     
    cv2.imshow("Webcam Feed", frame) #shows the live feed from camera
    
    key = cv2.waitKey(1) #Wait for 'c' to capture or 'q' to exit
    print(f"Press c to capture and q to exit")
    
    if key == ord('c'):
        cv2.imwrite("webcam.jpg", frame)#save image
        print(f"Image captured successfully")
        break
    elif key == ord('q'):
        print(f"Exiting without capture")#exit program
        break
    
    print(f"Done!")
    
imgcapture.release()
cv2.destroyAllWindows()