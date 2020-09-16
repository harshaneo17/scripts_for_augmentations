import cv2

# Opens the Video file
cap= cv2.VideoCapture('C:\\Users\\ASUS\\Downloads\\videokingstonproject\\Video1.mp4') 
i=1
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break
    if i%5 == 0:
        cv2.imwrite('kang'+str(i)+'.jpg',frame)
    i+=1

cap.release()
cv2.destroyAllWindows()
