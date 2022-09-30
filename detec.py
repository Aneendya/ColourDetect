#This is OpenCV project
#THIS PROGRAM DETECTS COLOUR IN A GIVEN IMAGE FILE
import numpy as np
import cv2
import argparse
def image_color():
    argumnets = argparse.ArgumentParser()
    argumnets.add_argument("-i", "--pic")
    args = vars(argumnets.parse_args())
    pic = cv2.imread(args["pic"])
    boundaries = [([17, 15, 100], [50, 56, 200]),([86, 31, 4], [220, 88, 50]),([25, 146, 190], [62, 174, 250]),([103, 86, 65], [145, 133, 128])]
    for (lowr, upr) in boundaries:
	    lowr = np.array(lowr, dtype = "uint8")
	    upr = np.array(upr, dtype = "uint8")
	    mask = cv2.inRange(pic, lowr, upr)
	    out = cv2.bitwise_and(pic, pic, mask = mask)
	    cv2.imshow("images", np.hstack([pic, out]))
	    cv2.waitKey(0)
image_color()
