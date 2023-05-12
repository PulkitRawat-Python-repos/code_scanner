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
    cv.waitkey(0)
#     Data= obj.dat
#     return Data

def create_qr_code():
    img=qrcode.make("https://www.youtube.com/")
    print(type(img))
    print(img.size)
    img.save('/qrcodec.png')

def create_bar_code():
    my_code = EAN13("5901234123457", writer=ImageWriter())
    my_code.save("/barcodec")  

# create_bar_code()
# data = read_code("/barcodec.png")
# print(data)
# create_qr_code()
# data = read_code("/qrcodec.png")
# print(data)
