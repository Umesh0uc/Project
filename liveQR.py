from pyzbar.pyzbar import decode
import cv2
import time
import datetime
import sys
import os
#initializing camera for video capturing
cap = cv2.VideoCapture(0)
todayDate = datetime.date.today()
fileName = "busAtt"+str(todayDate)+".csv"
print(fileName)
f = None
if os.path.isfile(fileName):
    f = open(fileName,"a")
else:
    f = open(fileName,"w")
    f.write("BUS_NO,TIME\n")
while True:
    flag, img = cap.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    qrs_detected = decode((img))
    for qr in qrs_detected:
        xup,yup = qr.rect.left,qr.rect.top
        xdown,ydown = xup + qr.rect.width + 5 , yup + qr.rect.height + 5
        data = qr.data.decode('utf-8')
        if os.path.isfile(fileName):
            f = open(fileName,"a")
        else:
            f = open(fileName,"w")
            f.write("BUS_NO,TIME")
        f.write(data+","+str(time.ctime()[11:19])+"\n")
        cv2.rectangle(img, (xup-5,yup-5), (xdown,ydown), (243,23,45))
        cv2.putText(img, data, (xup-15,yup-15),cv2.FONT_HERSHEY_PLAIN,1,(24,45,67),2)
        time.sleep(1)
        f.close()
        break

    cv2.imshow("QR detector",img)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()