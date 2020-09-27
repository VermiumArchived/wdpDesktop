# -*- coding: utf-8 -*-
# WhatsDisPic?

from deps import * # Importing all dependencies from deps.py
from config import general # User configuration - Local file (config.py)
from ai import runAI
from dominant import runDominant
from palette import runPalette
from moveOriginal import *
from progressBar import *

clear = lambda: os.system('cls') # Define clear() as cls

total = 0
current = 0

for root, dirs, files in os.walk(general['root'], topdown=False):
    for name in [fi for fi in files if fi.lower().endswith(tuple(general['fileTypes']))]:
        total += 1
progress = ProgressBar(int(total), fmt=ProgressBar.FULL)
for root, dirs, files in os.walk(general['root'], topdown=False):
    for name in [fi for fi in files if fi.lower().endswith(tuple(general['fileTypes']))]:
        progress.current = current
        progress()
        base, ext = os.path.splitext(name) # Split file up into base.ext

        try: # Create directory root/picture/
            os.mkdir(root + "\\" + base) # Create directory for image root/picture/
        except: pass # Pass, if error/already exists

        runAI(
            name,
            root,
            base,
            ext
        ) # Runs AI code
        runDominant(
            name,
            root,
            base,
            ext
        ) # Runs Dominant code
        runPalette(
            name,
            root,
            base,
            ext
        ) # Runs Palette code
        moveOriginal(name, root, base, ext) # Runs moveOriginal code

        # Printing some properties about the image

        print(
            "Image Name: %s" % str(name) + # Prints name of image
            "\nProgress: %s/%s" % (str(current), str(total)) +
            "\nProgressPercentage %s" % (str(int(total) //100 * int(current)))
        )
        progress()
        sleep(1)
        clear()
        current += 1
##        progress.done()