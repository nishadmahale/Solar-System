import cv2
img=cv2.imread("solar-system.jpg")
cv2.imshow("output",img)

cv2.waitKey(0)

cv2.putText(img,"Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255, 87, 51 ))
cv2.putText(img,"Mecury",(30,400),cv2.FONT_HERSHEY_COMPLEX,0.5,(255, 87, 51 ))
cv2.putText(img,"Venus",(40,500),cv2.FONT_HERSHEY_COMPLEX,0.5,(255, 87, 51 ))
cv2.putText(img,"Earth",(50,600),cv2.FONT_HERSHEY_COMPLEX,0.5,(255, 87, 51 ))
cv2.putText(img,"Mars",(60,700),cv2.FONT_HERSHEY_COMPLEX,0.5,(255, 87, 51 ))
cv2.putText(img,"Jupiter",(70,800),cv2.FONT_HERSHEY_COMPLEX,0.5,(255, 87, 51 ))
cv2.putText(img,"Saturn",(80,900),cv2.FONT_HERSHEY_COMPLEX,0.5,(255, 87, 51 ))
cv2.putText(img,"Uranus",(90,1000),cv2.FONT_HERSHEY_COMPLEX,0.5,(255, 87, 51 ))
cv2.putText(img,"Neptune",(100,1200),cv2.FONT_HERSHEY_COMPLEX,0.5,(255, 87, 51 ))

cv2.imwrite("Solar_systemwithname.jpg",img)
            