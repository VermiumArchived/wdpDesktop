from deps import * # Importing all dependencies from deps.py
from config import enablePalette

def palette(name, root, base, ext):
    if enablePalette:
        palette = "" # Init pattern variable

        im = Image.open(root + '\\' + name) # Opening root/picture.ext
        width, height = im.size # Taking the width of that pictures
        im.close() # Closing the opened image root/picture.ext

        color_thief = ColorThief(root + '\\' + name) # Getting image's color-properties
        palette = color_thief.get_palette(color_count=6)

        print(
            "\nImage Palette: %s" % str(palette) # Prints Image Pattern
        )