import qrcode
import cv2 as cv
from pyzbar.pyzbar import decode
from barcode import EAN13
from barcode.writer import ImageWriter

def read_code(filepath): 
    img = cv.imread(filepath)
    scan = decode(img)
    for obj in scan:
        print("Type:",obj.type)
        print("Data:",obj.data,"/n")
    cv.imshow("code", img)
    Data= obj.data
    return Data

def create_qr_code():
    img=qrcode.make("https://www.youtube.com/")
    print(type(img))
    print(img.size)
    img.save('/qrcodec.png')
# create_bar_code()co
# data = read_code("/barcodec.png")
# print(data)
# create_qr_code()
# data = read_code("/qrcodec.png")
# print(data)