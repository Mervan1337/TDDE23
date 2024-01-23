import cv2
import cvlib
import numpy
import random
from lab5a import *

def create_lock(indata, statement):
    """ Creates a lock where you need to type in correct pin code to unlock """
    pin = indata
    def correctlock(pin):
        if indata == pin:
            print(statement)
        else:
            print("Fel kod")
    return correctlock

def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """ Sets an allowed hsv value where it returns 1 if it meets it condition but returns 0 if it wont meet the criteria """
    def correcthsv(hsv):
        if not isinstance(hsv, tuple):
            raise TypeError("Tuple error")
        try:    
            h, s, v = hsv
            if h > hlow and hhigh > h:
                if s > slow and shigh > s:
                    if v > vlow and vhigh > v:
                        return 1
                    else:
                        return 0
                else:
                    return 0
            else:
                return 0
        except TypeError as e:
            raise e
        except ValueError as e:
            raise e
    return correcthsv

def cvimg_to_list(img):
    """ Converts image img to a list of tuples """
    dimension = img.shape
    color = []
    for x in range(dimension[0]):
        for y in range(dimension[1]):
            color.append(tuple(img[x, y]))
    return color

def generator_from_image(img):
    """ Takes in a image consisting of tuples and returns a function which gathers a specific rgb/bgr on pixel index """
    def generated_img(index):
        if not isinstance(index, tuple):
            raise TypeError("Tuple error")
        try:    
            rgb = img[index]
            return rgb
        except IndexError as e:
            raise e
        except TypeError as e:
            raise e
    return generated_img

def combine_images(hsv_list, condition, generator1, generator2):
    """ Makes a new list which is filled with new tuple values to combine two images based on hsv_list and the condition """
    try:
        new_bgr = []
        for i in range(len(hsv_list)):
            bgr = cvlib.add_tuples(
                cvlib.multiply_tuple(generator1(i), condition(hsv_list[i])), 
                cvlib.multiply_tuple(generator2(i), 1 - condition(hsv_list[i]))
            )
            new_bgr.append(bgr)
        return new_bgr
    except IndexError as e:
        raise e
    except TypeError as e:
        raise e
    except ValueError as e:
        raise e

def gradient_condition(bgr):
    """ Creates a new mask based on the bgr input """
    if not isinstance(bgr, tuple):
        raise TypeError("Tuple error")    
    try:
        b, g, r = bgr
        gradient_bgr = (b/256+g/256+r/256)/3
        return gradient_bgr
    except TypeError as e:
        raise e
    except ValueError as e:
        raise e

# Ls in bilderna
plane_img = cv2.imread("plane.jpg")
rose_img = cv2.imread("flowers.jpg")
gradient_img = cv2.imread("gradient.jpg")

# Skapa ett filter som identifierar himlen

# Omvandla originalbilderna till en lista med HSV-färger
plane_img_list = cvimg_to_list(plane_img)
rose_img_list = cvimg_to_list(rose_img)
gradient_bgr_list = cvimg_to_list(gradient_img)

# Skapa en generator som gör en stjärnhimmel
generator1 = generator_from_image(rose_img_list)

# Skapa en generator för den inlästa bilden
generator2 = generator_from_image(plane_img_list)

# Kombinera de två bilderna till en, alltså använd himmelsfiltret som mask
#result = combine_images(gradient_bgr_list, gradient_condition, generator1, generator2)

# Omvandla resultatet till en riktig bild och visa upp den
#new_img = cvlib.rgblist_to_cvimg(result, plane_img.shape[0], plane_img.shape[1])
#cv2.imshow('Final image', new_img)
#cv2.waitKey(0)
        
# Testing generator_from_image with three tuples and a nested list
test_generator_from_image = generator_from_image((30, 42, 42))
try:
    result = test_generator_from_image([123])
except TypeError:
    print("OK!")
try:
    result = test_generator_from_image((123, 123, 123, 123))
except TypeError:
    print("OK!")

# Testing pixel_constraint with three tuples and a nested list
test_pixel_constrait = pixel_constraint(50,50,50,50,50,50)
try:
    result = test_pixel_constrait([234])
except TypeError:
    print("OK!")
try:
    result = test_pixel_constrait((43,43,43,34))
except ValueError:
    print("OK!")

# Testing gradient_conditionwith three tuples and a nested list
try:
    test_gradient_condition = gradient_condition([234])
except TypeError:
    print("OK!")
try:
    test_gradient_condition = gradient_condition((54,54,54,54))
except ValueError:
    print("OK!")

# Testing combine_imageswith three tuples and a nested list
try:
    test_combine_images = combine_images((54,43,43,43), gradient_condition, generator_from_image(rose_img), generator_from_image(plane_img_list))
except TypeError:
    print("OK!")
try:
    test_combine_images = combine_images([212], gradient_condition, generator_from_image(rose_img), generator_from_image(plane_img_list))
except TypeError:
    print("OK!")
print("The code can handle all testcases.")
