#import the required libraries
import numpy as np
import cv2
import glob
import os
from matplotlib import pyplot as plt
from PIL import Image

#give the in and out directories 

#change the input directolry to where you have all your images that you want to work on
input_dir="D:\workspace\school\Surrey\pedobaro\codebase\Ractangle_screenshot_extraction"

#change this to where you  want to make output folder
output_dir="D:\workspace\school\Surrey\pedobaro\codebase\Ractangle_screenshot_extraction"

#traverse through the given directory and make a list of names with jpg extention

os.chdir(output_dir)     #change dir to outpt dir and make a folder of the name cropped
if not os.path.isdir("cropped"):
                    os.mkdir("cropped")


os.chdir(input_dir)      #change the directory to input folder and get the list of names with jpg extention
files=glob.glob("*.jpg")
#print(files)

#main for loop that traverse through all the files and saves them into ouput directory

for n in files:

    #read the image into the envoirnment one by one code to manipulate
    img =cv2.imread(n)

    #convert the color image to greyscale for thresholding later
    #helpfull as we need to crop color image in the end thats why instead of opeing image directly in greyscale we load in colour get contours in grey scale 
    #and then crop the color image and save back according to the contours we got
    img_gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY);
    
    
    #binary thresholding
    ret,thresh = cv2.threshold(img_gray,0,255,cv2.THRESH_BINARY)

    #getting a list of contours using opencv find contours
    IMAGE,contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE,  cv2.CHAIN_APPROX_SIMPLE)

    #sorts all the contours in desecnding order and get only two of the largest contours whcih are 1-whole image and 2-ROI
    # we only take the second highest ractangle using key ContourArea and plot that.
    cnt = sorted(contours, key = cv2.contourArea, reverse = True)[1:2]

    for c in cnt:
        x,y,w,h = cv2.boundingRect(c)


        x2 = x+w+5    #added these 5 pixels padding to the height and width of the image
        y2 = y+h

    

    #plot and check if the image has been loaded correctly
    #plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    
    #cropping the orignal colour image from the size of ROI we got from cv2-contours
    cropped_img = img[y:y+h, x:x+w]
    
    #write the required part of image as a seprate image after the extraction 
    cv2.imwrite(output_dir+'/cropped/'+n,cropped_img)