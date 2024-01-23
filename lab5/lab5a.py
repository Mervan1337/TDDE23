import cv2
import cvlib
import math
import numpy
def cvimg_to_list(img):
    dimension = img.shape
    color = []
    for i in range(dimension[0]):
        for j in range(dimension[1]):
            color.append(tuple(img[i,j]))
    return color

def unsharp_mask(N):
    lower_N = -(N//2)
    upper_N = N//2
    if N % 2 == 0:
        upper_N -= 1
    list = [[1.5 if (y,x) == (0,0) else formula(y,x) for y in range(lower_N,upper_N)] for x in range(lower_N,upper_N)]
    return list

def formula(x,y):
    return -((1/(2*math.pi*4.5**2))*(math.e**(-(x**2+y**2)/(2*4.5**2))))



#img = cv2.imread('plane.jpg')
#kernel = numpy.array(unsharp_mask(20))
#filtered_img = cv2.filter2D(img, -1, kernel)    
#cv2.imshow("filtered", filtered_img)
#cv2.waitKey(0)