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
print(img_ar)
