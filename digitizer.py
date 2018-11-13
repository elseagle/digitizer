import cv2
import sys, os, glob
import pytesseract
from pytesseract import image_to_string
from docx import Document

# import glob, os
# os.chdir("/mydir")
# for file in glob.glob("*.txt"):
#     print(file)


if __name__ == "__main__":
    doc_file = Document()
    command_length = len(sys.argv) 

    if command_length < 2 :
        print ("Usage: python digitizer.py <image-name>.jpg")
        sys.exit(1)
        # if not os.path.exists(directory):
        #     print ("making directory")
        #     os.makedirs(directory)
        #     doc_file.save(file_path)

    image_path = sys.argv[1]
    cmd = "/usr/bin/tesseract"
    # '-l eng'  for using the English language
    # '--oem 1' for using LSTM OCR Engine
    config = ('-l eng --oem 1 --psm 3')
    image = cv2.imread(image_path, cv2.IMREAD_COLOR)

    text = image_to_string(image, config=config)

    if text:
        doc_file.add_paragraph(text)
        list_text = list(text)
        if len(text) >9:
            list_name = list_text[:6]
        else:
            list_name = list_text[:]
        name = ''.join(list_name)
        file_path = "{}.docx".format(name)
        # list_directory = list(file_path)
        # list_directory_create = list_directory[:31]
        # directory_create = "".join(list_directory_create)
        # directory = os.path.dirname(directory_create)
        # if not os.path.exists(directory):
        #     print ("making directory")
        #     os.makedirs(directory)
        #     doc_file.save(file_path)
        doc_file.save(file_path)

                
                    

        print(text)

    else:
        print("No text found. Make sure you have a good quality for your picture")
        




