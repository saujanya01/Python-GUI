import cv2
import numpy as np
import pytesseract

img=cv2.imread('/home/saujanya/OCR/practice/final/skew correction/rotated_image.png')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray=np.bitwise_not(gray)
(T,thresh)=cv2.threshold(gray,200,255,cv2.THRESH_BINARY)
cv2.imshow('After thresholding',thresh)

cord=np.column_stack(np.where(thresh>0))
angle=cv2.minAreaRect(cord)[-1]
if angle < -45:
    angle=-(angle+90)
else:
    angle=-angle

(h,w)=img.shape[:2]
center=(w//2 , h//2)
M=cv2.getRotationMatrix2D(center,angle,1.0)
rotated=cv2.warpAffine(img,M,(w,h),flags=cv2.INTER_CUBIC,borderMode=cv2.BORDER_REPLICATE)
(t,final)=cv2.threshold(rotated,200,255,cv2.THRESH_BINARY)
cv2.imwrite("Straight.png",final)

text=pytesseract.image_to_string(final)
print(text)

cv2.imshow('Rotated',final)
cv2.imshow('Original',img)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
error
Exception has occurred: cv2.error
OpenCV(3.4.3) /io/opencv/modules/imgproc/src/color.cpp:181: error: (-215:Assertion failed) !_src.empty() in function 'cvtColor' 
  File "/home/saujanya/codes/Python code/GUI using Tkinter/v.py", line 6, in <module>
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
  File "/home/saujanya/anaconda3/lib/python3.7/runpy.py", line 85, in _run_code
    exec(code, run_globals)
  File "/home/saujanya/anaconda3/lib/python3.7/runpy.py", line 96, in _run_module_code
    mod_name, mod_spec, pkg_name, script_name)
  File "/home/saujanya/anaconda3/lib/python3.7/runpy.py", line 263, in run_path
    pkg_name=pkg_name, script_name=fname)
'''