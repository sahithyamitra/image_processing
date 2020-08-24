import cv2,glob

all_images=glob.glob("*.jpg")
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
for i in all_images:
    img=cv2.imread()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(img,1.3,5)
    for (x,y,w,h) in faces:
        final_img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("face detector",final_img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
