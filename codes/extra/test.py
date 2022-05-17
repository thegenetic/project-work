import cv2
from PIL import Image
img = cv2.imread("C:/Users/HP/OneDrive/Pictures/id.jpg")
x,y,z = img.shape
 
# height, width, number of channels in image
# height = img.shape[0]
# width = img.shape[1]
# channels = img.shape[2]
# print (img.getpixel(coordinate)) 
print('Image Dimension    : ',x,y,z)
print(img.size)



#formulae
#(1+(1/q((1+q((1-x)/x)**k)**w-1))**(1/k))**(-1)