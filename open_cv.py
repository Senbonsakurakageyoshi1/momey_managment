import cv2
import numpy as np
import matplotlib.pyplot as plt
image = cv2.imread('/home/paindr/Desktop/pycharm-community-2021.3.2/bin/pycharm.png',1)

image1 = cv2.imread('/home/paindr/Desktop/pycharm-community-2021.3.2/bin/pycharm.png',1)

Kenpachi = cv2.imread('/home/paindr/Desktop/k.png', 1)

rib = cv2.imread('/home/paindr/Desktop/Liste RIB/RIBBoursorama Bank1.png')
h,w = image.shape[:2]
hr,wr  = rib.shape[:2]
hk,wk = Kenpachi.shape[:2]

kernel = np.ones((5,5),np.uint8)
print('the shape is : {} and the height is :{}'.format(h,w))

#extracting RGB values

b,g,r = image[27,27]

print('R={},G={},B={}'.format(r,g,b))

B = image[100,100,0]

print("B={}".format(B))

roi = image[50:50,50:50]

print(roi)

resize = cv2.resize(image,(800,800))

resize = cv2.imwrite('resize.png',resize)
print(resize)

#cv2.imshow('resize.png',resize)
center =(w//2,h//2)
matrix = cv2.getRotationMatrix2D(center,-45,1.0)

rotated = cv2.warpAffine(image,matrix,(w,h))
rotated = cv2.imwrite('rotated.png',rotated)
output = image.copy()
rectangle = cv2.rectangle(output,(40,55),(60,80),(0,255,0),20)

cv2.imwrite('output.png',output)

rotated=cv2.imread('rotated.png')
#cv2.imwrite('addition.png',cv2.addWeighted(image,0.5,rotated,0.8,10))
cv2.imwrite('addition.png',cv2.add(image,rotated))

cv2.imwrite('substration.png',cv2.subtract(image,rotated))

cv2.imwrite('add.png',cv2.bitwise_and(image,rotated,mask=None))

cv2.imwrite('or.png',cv2.bitwise_or(image,rotated,mask=None))
cv2.imwrite('xor.png',cv2.bitwise_xor(image,rotated,mask=None))
cv2.imwrite('not.png',cv2.bitwise_not(image,rotated,mask=None))


cv2.imwrite('zoom_rib1.png',cv2.resize(rib,(8*hr,4*wr),interpolation=cv2.INTER_NEAREST))
cv2.imwrite('zoom_rib2.png',cv2.resize(rib,(8*hr,4*wr),interpolation=cv2.INTER_CUBIC))
cv2.imwrite('zoom_rib3.png',cv2.resize(rib,(8*hr,4*wr),interpolation=cv2.INTER_LINEAR))
cv2.imwrite('zoom_rib4.png',cv2.resize(rib,(8*hr,4*wr),interpolation=cv2.INTER_LINEAR_EXACT))
print(type(image))






#image Processing in python (Scaling,Rotating,Shifting and edge detection)

cv2.imwrite('canny_kenpachi.jpg', cv2.Canny(Kenpachi, Kenpachi.shape[:2][0] * 2, Kenpachi.shape[:2][1] * 2))


#image blurring
rib_gaussian = cv2.GaussianBlur(cv2.resize(rib,(8*hr,4*wr),interpolation=cv2.INTER_CUBIC),(3,3),0)
rib_median = cv2.medianBlur(cv2.resize(rib,(8*hr,4*wr),interpolation=cv2.INTER_CUBIC),5)
cv2.imwrite('rib_gaussian.png',rib_gaussian )
cv2.imwrite('rib_median.png',rib_median)

#erosion and dilatation

img_erosion = cv2.erode(cv2.resize(rib,(16*hr,8*wr),interpolation=cv2.INTER_CUBIC),kernel,iterations=1)
img_dilatation = cv2.dilate(cv2.resize(rib,(8*hr,4*wr),interpolation=cv2.INTER_CUBIC),kernel,iterations=1)

cv2.imwrite('rib_erosion.png',img_erosion)
cv2.imwrite('rib_dilatation.png',img_dilatation)

#adaptative threshold method

thres1 = cv2.adaptiveThreshold(cv2.resize(rib,(16*hr,8*wr),interpolation=cv2.INTER_CUBIC),255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,10)
cv2.imwrite('rib_supreme.png',thres1)
#video with opencv

'''cap = cv2.VideoCapture('tree.mp4')

if (cap.isOpened()==False):
    print('La camera n est pas allumée')

while(cap.isOpened()):

    ret,frame = cap.read()
    if ret==True:
         cv2.imshow('Frame',frame)

         if cv2.waitkey(25)&0*ff== ord('q'):
             break
     else:
         break
cap.release()

cv2.destroyAllWindows()'''