#OCR-with-OpenCV
from pytesseract import Output
import pytesseract as pyt
import cv2
import argparse as arg
import imutils

# Construct the argument parser and parse the arguments
ap = arg.ArgumentParser()
ap.add_argument("-i","--image", required=True, help="path to input image to be OCR'd")
args = vars(ap.parse_args())

# load th input image, convert it from BGR to RGB channel ordering, and use Tesseract to determine the text orientation

image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

results = pyt.image_to_osd(rgb, output_type=Output.DICT)

#Display the orientation information
print(f"[INFO] detected orientation: {results['orientation']}")

print(f"[INFO] rotate by {results['rotate']} degrees to correct.")

print(f"[INFO] detected script: {results['script']}")

# Rotote the image to correct the orientation
rotated = imutils.rotate_bound(image, angle=results["rotate"])

# show the original image and output image after orienation
# correction
cv2.imshow("Original", image)
cv2.imshow("Output", rotated)
cv2.waitKey(1)
