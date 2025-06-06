#OCR-with-OpenCV/whitelist_blacklist.py

import pytesseract as pyt
import argparse as arg
import cv2

# Construct the argument parser and parse the arguments 
ap = arg.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to imput image to be OCR'd")
ap.add_argument("-w","--whitelist",type=str, default="",help="list of characters to whitelist")
ap.add_argument("-b","--blacklist", type=str, default="", help ="list of characters to blacklist")

args = vars(ap.parse_args())

image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
options = ""

#Check to see if a set of whitelist charcters has been provided, and if so update our options string
if len(args["whitelist"]) > 0:
    options += f"-c tessedit_char_whitelist={args['whitelist']}"

# Check to see if a set of blacklist characters has been provided, and if so, update our options string
if len(args["blacklist"]) > 0:
    options += f"-c tessedit_char_blacklist={args['blacklist']}"

# OCR the input image using Tesseract
text = pyt.image_to_string(rgb, config=options)
print(text)

