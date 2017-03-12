import numpy
import sys
import os
import cv2

#module level variables ######

MIN_CONTOUR_AREA = 100

RESIZED_IMAGE_WIDTH = 20
RESIZED_IMAGE_WIDTH = 30

################################
def  main():
	imgTrainingNumbers = cv2.imread("training_chars.png") 

	if imgTrainingNumbers is None:
		print "error: image not found"
		os.system("pause")
		return

	imgGray = cv2.cvtColor(imgTrainingNumbers,cv2.COLR_BGR2GRAY)
	imgBlurred = cv2.GaussianBlur(imgGray,(5,5),0)

	imgThresh = cv2.adaptiveThreshold(imgBlurred,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,11,2)

	cv2.imshow("imgThresh",imgThresh)