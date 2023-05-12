
import cv2 as cv
from pyzbar.pyzbar import decode

def read_qr_code(filepath):
    img = cv.imread(filepath)
    scan = decode(img)
    for obj in scan:
        print("Type:",obj.type)
        print("Data:",obj.data,"/n")
    cv.imshow("code", img)
    Data= obj.data
    return Data




data = read_qr_code("qrcode.png")
print(data)