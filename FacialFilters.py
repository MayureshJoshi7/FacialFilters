import cv2
face1 = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
face2 = cv2.CascadeClassifier('haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

ch = int(input("Enter choice: "))


repl1 = cv2.imread('mask4.png')

repl2 = cv2.imread('laser.png')

repl2 = cv2.imread('Eyes.png')


while True: 
    ret,frame = cap.read()
    frame = cv2.flip(frame,1)
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    if ch == 1:
        f = face1.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors = 7)
    elif ch == 2:
        f = face2.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors = 7)
    elif ch == 3:
        f = face2.detectMultiScale(gray,scaleFactor = 1.1,minNeighbors = 7)
        
    for x,y,w,h in f:

        if ch == 1:
            repl1 = cv2.resize(repl1,(w,h))
            frame[y:y+w,x:x+h] = repl1
            cv2.imshow('Face Recognized',frame)


        elif ch == 2:
            repl2 = cv2.resize(repl2,(w,h))
            frame[y:y+w,x:x+h] = repl2
            cv2.imshow('Face Recognized',frame)

        elif ch == 3:
            repl3 = cv2.resize(repl3,(w,h))
            frame[y:y+w,x:x+h] = repl3
            cv2.imshow('Face Recognized',frame)
        
    if cv2.waitKey(1) == ord('q'):
        break



cap.release()          
cv2.destroyAllWindows()
