from PIL import Image, ImageFilter
import numpy as np
import cv2


in_path = input("Write path to image: ")
out_path = input("Write path to output folder: ")

def read_and_convert_to_data(path):
    img_file_open = Image.open(path)
    img_numpy_data = np.array(img_file_open)
    img_array = Image.fromarray(img_numpy_data)
    return img_array

def normal(img):
    return np.array(img)

def filter_contour(img):
    return img.filter(ImageFilter.CONTOUR)

def filter_detail(img):
    return img.filter(ImageFilter.DETAIL)

def filter_edge(img):
    return img.filter(ImageFilter.EDGE_ENHANCE)

def filter_sharpen(img):
    return img.filter(ImageFilter.SHARPEN)

def filter_smooth(img):
    return img.filter(ImageFilter.SMOOTH_MORE)

def  apply_list_of_func (func_list,argument):

    result = []

    for f in func_list:
        result.append(np.array(f(argument)))

    return result

#Create seria of images
filter_list = [normal, filter_smooth, filter_sharpen, filter_detail, filter_edge, filter_contour]
img = read_and_convert_to_data(in_path)
seria_of_img = apply_list_of_func(filter_list, img)

#Create VideoWriter object
cv2.imshow('video',np.array(img))
height, width, channels = np.array(img).shape
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter(out_path + "Converted_image_seria.mp4", fourcc, 1.5, (width, height))

for image in seria_of_img:
    out.write(cv2.cvtColor(image, cv2.COLOR_RGB2BGR))
out.release()
