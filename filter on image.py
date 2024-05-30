import random as np 
import matplotlib.pyplot as plt
from PIL import Image ,ImageFilter

img=Image.open("D:/imp/Taha Ali Bawahir .jpg")
print(img.show)

img2=img.filter(ImageFilter.BLUR)
print(img2.show)

img3=img.filter(ImageFilter.CONTOUR)
print(img3.show)

img3=img.filter(ImageFilter.EMBOSS)
print(img3.show)

img2=img.filter(ImageFilter.BLUR)
print(img2.show)

imgsplit=Image.Image.split(img)
imgsplit[0].show
imgsplit[1].show
imgsplit[2].show

img_ar=np.array(img)
plt.imshow(img_ar[:,:,0],cmap='gray')
