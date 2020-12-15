import os
from PIL import Image, ImageEnhance, ImageFilter
import matplotlib.pylab as plt

os.chdir(os.path.join("data", "obj"))
for fname in os.listdir(os.getcwd()):
  if fname.endswith(".jpg"):
    img = Image.open(fname)
    for x in range(0,img.size[0]):
      for y in range(0,img.size[1]):
        rgb = img.getpixel((x,y))
        rgb_wb = round((rgb[0]+rgb[1]+rgb[2])/3)
        img.putpixel((x,y), (255-rgb_wb, 255-rgb_wb, 255-rgb_wb))
    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(0.5)
    bright = ImageEnhance.Brightness(img)
    img = bright.enhance(0.9)
    img = img.filter(ImageFilter.BoxBlur(5))
    print("Modify: " + os.getcwd() + fname)
    img.save(fname[:-4] + "-1.jpg")
  elif fname.endswith(".txt"):
    print("Copy: " + os.getcwd() + fname)
    os.system("cp " + fname + " " + fname[:-4] + "-1.txt")

os.chdir(os.path.join("..", ".."))
