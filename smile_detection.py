import cv2,glob

detect = cv2.CascadeClassifier("haarcascade_smile.xml")
imp_img = cv2.VideoCapture("elon.jpg")
res,img = imp_img.read()
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=detect.detectMultiScale(gray,1.3,5)
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imshow("fisrt image",img)
cv2.waitKey(0)
imp_img.release()
cv2.destroyAllWindows()
