'''''''''
image 8 bit to 16 bit

if there are case is a 12 bit image
the image will to 8 bit image. then, the image change to 16 bit image.
the result proven wit imageJ.
the image type is 16 bit and range value pixel 0 to 655535 

'''''


import numpy as np
import cv2

#input image
image=cv2.imread('Image8bit.tiff',cv2.COLOR_BGR2GRAY)

#image 12 bit to 8 bit
img=np.array(image,dtype=np.uint8)
img=cv2.normalize(img,dst=None, alpha=0,beta=255,norm_type=cv2.NORM_MINMAX)
print(img.dtype)

#image 8 bit to 16 bit
img=np.array(img,dtype=np.uint16)
img=cv2.normalize(img,dst=None, alpha=0,beta=65535,norm_type=cv2.NORM_MINMAX)
print(img.dtype)

# result
cv2.imwrite('Image16bit.tiff',img)
