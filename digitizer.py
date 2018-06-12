import cv2
import sys
from pytesseract.pytesseract import tesseract_cmd as cmd
from pytesseract import image_to_string


if __name__ == "__main__":
    command_length = len(sys.argv) 

    if command_length < 2 :
        print ("Usage: python digitizer.py <image-name>.jpg")
        sys.exit(1)

    image_path = sys.argv[1]
    cmd = "/usr/bin/tesseract"
    # '-l eng'  for using the English language
    # '--oem 1' for using LSTM OCR Engine
    config = ('-l eng --oem 1 --psm 3')
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    text = image_to_string(image, config=config)

    if text:
        print(text)
    else:
        print("No text found. Make sure you have a good quality for your picture")
        




