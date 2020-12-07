import cv2
import numpy as np

path='E:\original\Resolute AI\Open CV\Task_5_Towel_Counting.mp4'
cap=cv2.VideoCapture(path)
img=cv2.imread('E:\original\Resolute AI\Open CV\\test.png')
"""""""""
while True:
    success, img=cap.read()
    cv2.imshow("output",img)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
"""""""""

def empty():
    pass

cv2.namedWindow("Trackerbars")
cv2.resizeWindow("Trackerbars",640,240)

cv2.createTrackbar("Threshold 1","Trackerbars",10,255,empty)
cv2.createTrackbar("Threshold 2","Trackerbars",10,255,empty)



ret, frame1=cap.read()
ret, frame2=cap.read()


while cap.isOpened():
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)

    _,thresh=cv2.threshold(blur,26,80,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=1)
    #canny=cv2.Canny(blur,t1,t2)
    contours,_=cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 400:
            cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(approx)
            x ,y ,w , h=cv2.boundingRect(approx)
            rekt=cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,0,0),5)
            arr = []
            nuarr = []
            n = 0
            for i in rekt:
                arr.append(n + 1)
            print("arr", len(arr) / 352)
            print("type", type(rekt))
            nuarr.append(len(arr) / 352)


    cv2.imshow("Output",frame1)
    frame1=frame2
    ret,frame2  =cap.read()
    print("type", type(rekt))
    if cv2.waitKey(300) & 0xFF==ord('q'):
        break
print(len(nuarr))



"""""""""""
while True:
    success, img=cap.read()

    blur=cv2.GaussianBlur(img,(7,7),1)
    gray=cv2.cvtColor(blur,cv2.COLOR_BGR2GRAY)

    t2 = cv2.getTrackbarPos("Threshold 2", "Trackerbars")
    canny=cv2.Canny(gray,50,84)

    _,thresh=cv2.threshold(canny,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)

    contours, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 1000:
            cv2.drawContours(img, contours, -1, (0, 255, 0), 2)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
            print(approx)
            x ,y ,w , h=cv2.boundingRect(approx)
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),5)


    cv2.imshow("Output", img)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
"""""""""""
"""""""""""
diff=cv2.absdiff(frame1,frame2)
gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)

_,thresh=cv2.threshold(blur,26,80,cv2.THRESH_BINARY)
dilated=cv2.dilate(thresh,None,iterations=1)
#canny=cv2.Canny(blur,t1,t2)
contours,_=cv2.findContours(dilated,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 800:
        cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)
        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)
        print(approx)
        x ,y ,w , h=cv2.boundingRect(approx)
        rekt=cv2.rectangle(frame1,(x,y),(x+w,y+h),(255,0,0),5)
        arr=[]
        n=0
        for i in rekt:
            arr.append(n+1)
        print("arr",len(arr)/352)
        print("type",type(rekt))

        cv2.imshow("Output",frame1)
        cv2.waitKey(0)
"""""""""""""""