import os
from PIL import Image, ImageFile, ImageEnhance, ImageFilter
import matplotlib.pylab as plt

ImageFile.LOAD_TRUNCATED_IMAGES = True

os.chdir(os.path.join("data", "obj"))
n = 1
for fname in os.listdir(os.getcwd()):
  if fname.endswith(".jpg"):
    print("Modify: " + os.getcwd() + "/" + fname + " (" + str(n) + ")")
    n = n + 1
    img = Image.open(fname)
    img = img.convert('RGB')
    for x in range(0,img.size[0]):
      for y in range(0,img.size[1]):
        rgb = img.getpixel((x,y))
        rgb_wb = round((rgb[0]+rgb[1]+rgb[2])/3)
        img.putpixel((x,y), (255-rgb_wb, 255-rgb_wb, 255-rgb_wb))
    contrast = ImageEnhance.Contrast(img)
    img = contrast.enhance(0.5)
    bright = ImageEnhance.Brightness(img)
    img = bright.enhance(0.9)
    img = img.filter(ImageFilter.BoxBlur(3))
    img.save(fname[:-4] + "-1.jpg")
  elif fname.endswith(".txt"):
    print("Copy: " + os.getcwd() + "/" + fname + " (" + str(n) + ")")
    n = n + 1
    os.system("cp " + fname + " " + fname[:-4] + "-1.txt")

os.chdir(os.path.join("..", ".."))
