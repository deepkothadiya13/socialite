import numpy as np
import cv2
from PIL import Image

def black_and_white_dithering(input_image_path,
                              output_image_path,
                              dithering=False):
    color_image = Image.open(input_image_path)
    if dithering:
        bw = color_image.convert("1")
    else:
        bw = color_image.convert("1",dither=Image.NONE)
    bw.save(output_image_path)


if __name__ == '__main__':
    black_and_white_dithering(
        'Steel Rod Profiles\\IMG_20190514_162007.jpg', #please put image location here
        'bw_caterpillar_dithering.jpg')


img = cv2.imread('bw_caterpillar_dithering.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

ret,thresh = cv2.threshold(gray,127,255,0)
# t2 = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2) #2nd option for threshold
# t3= cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2) #3rd optionn for thresold
contours,h = cv2.findContours(thresh,0,1)
counter_circle = 1
counter_square = 1
counter_rectangle = 1
counter_angle = 1
for cnt in contours:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)
    print(len(approx))
    if len(approx)==3 or len(approx)==2:
        counter_angle = counter_angle + 1
        cv2.drawContours(img,[cnt],0,(0,255,0),-1)
    elif len(approx)==4:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        if ar >= 0.95 and ar <=1.05:
            counter_square = counter_square + 1
        else:
            counter_rectangle = counter_rectangle + 1
        cv2.drawContours(img,[cnt],0,(0,0,255),-1)
    elif len(approx) == 9:
        counter_circle = counter_circle + 1
        cv2.drawContours(img,[cnt],0,(255,255,0),-1)
    elif len(approx) > 15:
        counter_circle = counter_circle + 1
        cv2.drawContours(img,[cnt],0,(0,255,255),-1)

print("rods", counter_square)
print("plates", counter_rectangle)
print("pipes", counter_circle)
print("angles", counter_angle)
imS = cv2.resize(gray, (960, 540))
cv2.imshow('img',imS)
cv2.waitKey(0)
cv2.destroyAllWindows()
