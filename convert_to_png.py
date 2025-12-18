from PIL import Image
import os

directory = os.getcwd()
for filename in os.listdir(directory):
    if filename.endswith(".jpg"):
        im = Image.open(filename)
        name = filename[:-4]
        im.save(name + '.png')

