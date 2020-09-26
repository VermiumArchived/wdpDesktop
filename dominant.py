from deps import * # Importing all dependencies from deps.py
from config import enableDominant

def dominant(name, root, base, ext):
    if enableDominant:
        dominantColor = "" # Init dominantColor variable

        im = Image.open(root + '\\' + name) # Opening root/picture.ext
        width, height = im.size # Taking the width of that pictures
        im.close() # Closing the opened image root/picture.ext

        color_thief = ColorThief(root + '\\' + name) # Getting image's color-properties
        dominantColor = color_thief.get_color(quality = 1) # Getting the image dominant color   

        ima = Image.new("RGB", (width, height), (dominantColor)) # Creating a image base with dominant color
        ima.save(root + "\\" + base + "\\" + "dominantColor" + ext) # Saves the dominant color image in root/picture/dominant.ext
        ima.close() # Close dominant image

        print(
            "\nDominant Color: %s" % str(dominantColor) # Prints Dominant color
        )