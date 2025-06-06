# OCR-with-OpenCV/ocr_digits.py

# Import the necessary packages
import pytesseract as pyt
import argparse as arg
import cv2

# Construct the argument parser and parse the arguments
ap = arg.ArgumentParser()
ap.add_argument(
    "-i", "--image", required=True, help="path to input image to OCR'd"
)  # --image -> A path to the image to be OCR'd
ap.add_argument(
    "-d",
    "--digits",
    type=int,
    default=1,
    help="whether or not *digits only* OCR will be performed",
)  # A flag indicating whether or not we should OCR digits only (by default, the option is et to a True Boolean)
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
options = ""

# Check to see if * digits only * OCR should be performed, and if so,
# update our Tesseract OCR options
if args["digits"] > 0:
    options = "outputbase digits"

# OCR the input image using Tesseract
text = pyt.image_to_string(rgb, config=options)
print(text)
