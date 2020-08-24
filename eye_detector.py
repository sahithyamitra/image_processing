import cv2,glob

detector=cv2.CascadeClassifier("haarcascade_eye.xml")
imp_img=cv2.VideoCapture("2.jpg")
res,img=imp_img.read()
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=detector.detectMultiScale(gray,1.1,2)
for x,y,w,h in faces:
    final_img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),5)
cv2.imshow("eye detection image",final_img)
cv2.waitKey(0)
imp_img.release()
cv2.destroyAllWindows()
