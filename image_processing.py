from PIL import Image
import os

def resize_image(path, width):
    img = Image.open(path)
    wpercent = (int(width)/float(img.size[0]))
    hsize = int((float(img.size[1])*float(wpercent)))
    img = img.resize((int(width),hsize), Image.ANTIALIAS)
    img.save(path)

def convert_image(path):
    base = os.path.splitext(path)[0]
    os.rename(path, base + '.jpg')