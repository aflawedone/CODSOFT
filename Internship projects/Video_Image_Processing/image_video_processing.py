import cv2 as cv

face_cap = cv.CascadeClassifier("C:/Users/Saradra/AppData/Roaming/Python/Python310/site-packages/cv2/data/haarcascade_frontalface_default.xml")

print("1--- Image processing")
print("2--- Video processing")

x = int(input("enter the choice: "))

match x:
    case 1:
        img_cap = cv.imread("ICT.jpeg")

        gray = cv.cvtColor(img_cap,cv.COLOR_BGR2GRAY)


        faces = face_cap.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=2,
            minSize=(1,1),
            flags=cv.CASCADE_SCALE_IMAGE
        )

        for (x,y,w,h) in faces:
           cv.rectangle(img_cap,(x,y),(x+w,y+h),(0, 0, 255), 2)
    
        print('number of faces found  =',len(faces))
        
        cv.imshow("Indian Cricket Team",img_cap)
        cv.waitKey(0)
        cv.destroyAllWindows()

    case 2: 
        video_cap = cv.VideoCapture(0)

        while True:
            ss, video_info = video_cap.read()
            col = cv.cvtColor(video_info, cv.COLOR_BGR2GRAY)
            faces = face_cap.detectMultiScale(
                col,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30,30),
                flags=cv.CASCADE_SCALE_IMAGE
            )
            for (x,y,w,h) in faces:
                cv.rectangle(video_info,(x,y),(x+w,y+h),(0, 0, 255), 2)
    
            cv.imshow("video_start",video_info)
            if cv.waitKey(10) == ord('a'):
                break
        video_cap.release()
    case 3 :
        print("WRONG CHOICE")

    


 