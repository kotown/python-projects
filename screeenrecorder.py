import cv2
import numpy as np #for arrays
from PIL import ImageGrab

def screenrecorder():
    fourcc = cv2.VideoWriter_fourcc(*'XVID')#4 character code that is used to create a video character object
    out = cv2.VideoWriter("Output.avi", fourcc, 5.0 , (1366, 768))#passing the name of recording, the video object, capture framerate and screen size
    
    while True:
        img = ImageGrab.grab()
        img_np = np.array(img) #convertin images to multi dimensional array
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)#color conversion
        cv2.imshow("Screen Recorder", frame)#shows screen recoding live
        out.write(frame) #saves the recording
        
        if cv2.waitKey(1)==27: #Exits immediately esc key is presses
            break
    out.release()
    cv2.destroyAllWindows()
    
screenrecorder()