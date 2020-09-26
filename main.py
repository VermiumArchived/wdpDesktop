# -*- coding: utf-8 -*-
# WhatsDisPic?

from deps import * # Importing all dependencies from deps.py
from config import * # User configuration - Local file (config.py)
from ai import *
from dominant import *
from palette import *
from moveOriginal import *

clear = lambda: os.system('cls') # Define clear() as cls

for root, dirs, files in os.walk(root, topdown=False):
    clear()
    for name in [fi for fi in files if fi.lower().endswith(tuple(fileTypes))]:

        base, ext = os.path.splitext(name) # Split file up into base.ext

        try: # Create directory root/picture/
            os.mkdir(root + "\\" + base) # Create directory for image root/picture/
        except: pass # Pass, if error/already exists

        ai(name, numGuess, root, base)
        dominant(name, root, base, ext)
        palette(name, root, base, ext)
        moveOriginal(name, root, base, ext)

        # Printing some properties about the image

        print(
            "Image Name: %s" % str(name) # Prints name of image
        )