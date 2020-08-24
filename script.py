import cv2

detect=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")#classifier
imp_img=cv2.VideoCapture("4.jpg")#importing image
res,img=imp_img.read()#reading image
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)#convert image to gray scale
faces=detect.detectMultiScale(gray,1.3,5)#get coordinates of image face where gray is image,1.3 is scale to fit,5 is thickness
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(120,80,0),2)#to draw rectangle img=image,(x,y)=tuple of starting-coordinates,(x+w,y+h)=tuple of end-coordinates,color,pixels
cv2.imshow("one image",img)#image show or print
cv2.waitKey(0)#to display in milliseconds
imp_img.release()#to release
cv2.destroyAllWindows()#to destroy the image window or to close it
