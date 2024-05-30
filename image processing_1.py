import numpy as np 
import matplotlib.pyplot as plt 
from PIL import Image

img=Image.open("D:/imp/Taha Ali Bawahir .jpg")
print(img)
print(type(img))
#colours
print(img.mode)

img_ar=np.array(img)
a=img_ar.shape
print(a)
#print(img_ar)

print(img.getbbox())
print(img.size)
print(img.format)
print(img.rotate(90))

img1=img.copy()
print(img.paste(img1,(100,100)))
print(img.resize(250,250))

crop_img=img.crop(0,0,10,25)
print(crop_img)
