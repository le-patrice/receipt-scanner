# OCR-with-OpenCV/first_ocr.py

# Import the necessary packages
import pytesseract as pyt
import argparse as arg
import cv2

# Construct the argument parser and parse the arguments
ap = arg.ArgumentParser()
ap.add_argument("-i","--image",required=True, help="path to input image to be OCR'd")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Use tesseract to ocr the image
text = pyt.image_to_string(image)
print(text)


